import customtkinter
import tkinter as tk
from tkinter import filedialog, simpledialog
import ast
import graphviz
import os
from GRASP.core import spell_check_code

class FlowchartGenerator(ast.NodeVisitor):
    """ Generate a flowchart of given code
    """
    def __init__(self):
        """ Initialize flowchart generator
        """
        self.graph = graphviz.Digraph(format="png")
        self.graph.attr(rankdir="TB") # TB: top to bottom
        self.node_count = 0
        self.node_stack = []
        self.var_assignments = {}

    def add_node(self, label):
        """ Add a node to the graph

        Keyword Arguments:
            label: 
        Returns:
            node_id:
        """
        node_id = f"node{self.node_count}"
        self.graph.node(node_id, label, shape="box", style="filled", fillcolor="lightblue")
        self.node_count += 1
        if self.node_stack:
            self.graph.edge(self.node_stack[-1], node_id)
        self.node_stack.append(node_id)
        return node_id

    def visit_FunctionDef(self, node):
        """ Controle function definition nodes

        Keyword Arguments:
            node:
        
        Returns:
            Nothing
        """
        func_node = self.add_node(f"Function: {node.name}()")
        self.generic_visit(node)
        self.node_stack.pop()

    def visit_If(self, node):
        """ Handle if statements

        Keyword Arguments:
            node:
        
        Returns:
            Nothing
        """
        self.add_node("If Condition")
        self.generic_visit(node)
        self.node_stack.pop()

    def visit_For(self, node):
        """ Handle for statements

        Keyword Arguments:
            node:
        
        Returns:
            Nothing
        """
        self.add_node("For Loop")
        self.generic_visit(node)
        self.node_stack.pop()

    def visit_While(self, node):
        """ Handle while statements

        Keyword Arguments:
            node:
        
        Returns:
            Nothing
        """
        self.add_node("While Loop")
        self.generic_visit(node)
        self.node_stack.pop()

    def visit_Assign(self, node):
        """ Handle variable assignments with labels

        Keyword Arguments:
            node:
        
        Returns:
            Nothing
        """
        if isinstance(node.targets[0], ast.Name):
            var_name = node.targets[0].id
            value_node = self.add_node(f"Assign: {var_name}")
            self.var_assignments[var_name] = value_node
            self.node_stack.pop()

    def visit_Name(self, node):
        """ Handle variables and connect to assigned value

        Keyword Arguments:
            node:
        
        Returns:
            Nothing
        """
        if node.id in self.var_assignments:
            self.graph.edge(self.var_assignments[node.id], self.node_stack[-1], label=node.id)

    def visit_Call(self, node):
        """ Handle function calls with labels
        
        Keyword Arguments:
            node:
        
        Returns:
            Nothing
        """
        if isinstance(node.func, ast.Name):
            func_name = node.func.id
            call_node = self.add_node(f"Call: {func_name}()")
            self.graph.edge(self.node_stack[-2], call_node, label=f"calls {func_name}()")
            self.node_stack.pop()

    def generate_flowchart(self, code):
        """ Generate flowchart from codde

        Keyword Arguments:
            node:
        
        Returns:
            Nothing
        """
        tree = ast.parse(code)
        self.visit(tree)
        return self.graph

def spell_check_ui(dictionary):
    """ Set the GUI of spell-checker

    Keyword arguments:
        dictionary: vocaburaly (words) which checked target words refer to
    
    Returns:
        Nothing
    """
    root = customtkinter.CTk()
    root.title("GRASP")
    root.geometry("700x1000")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    # area for input
    customtkinter.CTkLabel(root, text="🔤 Input Code:", anchor="w").pack(pady=(10, 0))
    
    text_frame = customtkinter.CTkFrame(root)
    text_frame.pack(pady=5, padx=10, fill="both", expand=True)

    text_area = tk.Text(text_frame, height=12, width=60, wrap="word", font=("Arial", 12))
    text_area.pack(side="left", fill="both", expand=True)

    text_scrollbar = tk.Scrollbar(text_frame, command=text_area.yview)
    text_scrollbar.pack(side="right", fill="y")
    text_area.config(yscrollcommand=text_scrollbar.set)
    
    button_frame = customtkinter.CTkFrame(root)
    button_frame.pack(pady=5)

    open_button = customtkinter.CTkButton(button_frame, text="📂 Open File", command=lambda: open_file(text_area))
    open_button.grid(row=0, column=0, padx=5)

    check_button = customtkinter.CTkButton(button_frame, text="✅ Check Spelling", command=lambda: append_tag(text_area, result_box, unique_box, dictionary))
    check_button.grid(row=0, column=1, padx=5)

    flowchart_button = customtkinter.CTkButton(button_frame, text="📊 Generate Flowchart", command=lambda: generate_flowchart(text_area))
    flowchart_button.grid(row=0, column=2, padx=5)

    # area for candidates of correctly-spelled
    customtkinter.CTkLabel(root, text="🔍 Spelling Suggestions:", anchor="w").pack(pady=(10, 0))
    result_box = customtkinter.CTkTextbox(root, height=100, width=480, wrap="word", state="disabled")
    result_box.pack(pady=5, padx=10)

    # area for unique expressions
    customtkinter.CTkLabel(root, text="🚀 Unique Expressions:", anchor="w").pack(pady=(10, 0))
    unique_box = customtkinter.CTkTextbox(root, height=100, width=480, wrap="word", state="disabled")
    unique_box.pack(pady=5, padx=10)
    root.mainloop()

def open_file(text_area):
    """ Open a file and display its contents

    Keyword Arguments:
        program_path: the path indicating the place of the program file (e.g. .py file) 
                    to be spell-checked
    
    Returns:
        Nothing
    """
    program_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")]) # especially only .py file
    if program_path:
        with open(program_path, "r", encoding="utf-8") as file:
            text_area.delete("1.0", customtkinter.END)
            text_area.insert(customtkinter.END, file.read())

def append_tag(text_area, result_box, unique_box, dictionary):
    """ Do spell-check and Append tags

    Keyword Arguments:
        Nothing
            
    Returns:
        Nothing
    """
    code = text_area.get("1.0", customtkinter.END)
    clean_code = remove_comments_and_docstrings(code)
    suggestions, unique_expressions = spell_check_code(clean_code, dictionary)

    # append tag to misspelled words
    text_area.tag_remove("misspelled", "1.0", tk.END)
    for word, suggestion in suggestions.items():
        start_index = "1.0"
        while True:
            start_index = text_area.search(word, start_index, stopindex=tk.END, nocase=True)
            if not start_index:
                break
            end_index = f"{start_index}+{len(word)}c"
            text_area.tag_add("misspelled", start_index, end_index)
            start_index = end_index

    text_area.tag_config("misspelled", underline=True, foreground="red")

    # show misspelled candidates
    result_text = "\n".join(f"'{word}' → '{suggestion}'" for word, suggestion in suggestions.items())
    result_box.configure(state="normal")
    result_box.delete("1.0", customtkinter.END)
    result_box.insert(customtkinter.END, result_text if result_text else "✅ No spelling errors found.")
    result_box.configure(state="disabled")

    # show unique expressions
    unique_text = "\n".join(f"'{word}'" for word in unique_expressions)
    unique_box.configure(state="normal")
    unique_box.delete("1.0", customtkinter.END)
    unique_box.insert(customtkinter.END, unique_text if unique_text else "🚀 No unique expressions found.")
    unique_box.configure(state="disabled")

def remove_comments_and_docstrings(code):
    """ Remove docstring and comments from the given Python code
    
    Keyword Arguments:
        code: program code

    Returns:
        code: the code to be returned after comments and docstrings are removed
    """
    import re
    code = re.sub(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', '', code)
    code = re.sub(r'#.*', '', code)
    return code

def generate_flowchart(text_area):
    """ Generate and display a flowchart from the code
    
    Keyword Arguments:
        text_area:
    
    Returns:
        Nothing
    """
    output_folder = filedialog.askdirectory(title="Select Folder to Save Flowchart")
    if not output_folder:
        print("❌ No folder selected. Flowchart not saved.")
        return
    
    filename = simpledialog.askstring("Save As", "Enter filename (without extension):")
    if not filename:
        print("❌ No filename entered. Flowchart not saved.")
        return
    
    code = text_area.get("1.0", customtkinter.END)
    clean_code = remove_comments_and_docstrings(code)
    generator = FlowchartGenerator()
    flowchart = generator.generate_flowchart(clean_code)
    
    os.makedirs(output_folder, exist_ok = True)
    output_path = os.path.join(output_folder, filename)
    flowchart.render(output_path, format="png", view=True)
    print(f"✅ Flowchart saved at: {output_path}.png")