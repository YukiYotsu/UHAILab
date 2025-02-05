import customtkinter
from tkinter import filedialog
from GRASP.core import spell_check_code

def spell_check_ui(dictionary):
    """ Set the GUI of spell-checker

    Keyword arguments:
        dictionary: vocaburaly (words) which checked target words refer to
    
    Returns:
        Nothing
    """
    root = customtkinter.CTk()
    root.title("GRASP")
    root.geometry("600x1000")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    # area for input
    customtkinter.CTkLabel(root, text="🔤 Input Code:", anchor="w").pack(pady=(10, 0))
    text_area = customtkinter.CTkTextbox(root, height=200, width=500, wrap="word")
    text_area.pack(pady=5, padx=10)

    open_button = customtkinter.CTkButton(root, text="📂 Open File", command=lambda: open_file(text_area))
    open_button.pack(pady=5)

    check_button = customtkinter.CTkButton(root, text="✅ Check Spelling", command=lambda: check_spelling(text_area, result_label, unique_box, dictionary))
    check_button.pack(pady=5)

    # area for candidates of correctly-spelled
    customtkinter.CTkLabel(root, text="🔍 Spelling Suggestions:", anchor="w").pack(pady=(10, 0))
    result_frame = customtkinter.CTkFrame(root)
    result_frame.pack(pady=5, padx=10, fill="both", expand=True)
    result_box = customtkinter.CTkTextbox(result_frame, height = 100, width = 480, wrap  = "word", state = "disabled")
    result_box.pack(side="left", fill="both", expand=True)

    result_scrollbar = customtkinter.CTkScrollbar(result_frame, command=result_box.yview)
    result_scrollbar.pack(side="right", fill="y")
    result_box.configure(yscrollcommand=result_scrollbar.set)

    # area for unique expressions
    customtkinter.CTkLabel(root, text="🐧 Unique Expressions:", anchor="w").pack(pady=(10, 0))
    unique_frame = customtkinter.CTkFrame(root)
    unique_frame.pack(pady=5, padx=10, fill="both", expand=True)

    unique_box = customtkinter.CTkTextbox(unique_frame, height=100, width=480, wrap="word", state="disabled")
    unique_box.pack(side="left", fill="both", expand=True)

    unique_scrollbar = customtkinter.CTkScrollbar(unique_frame, command=unique_box.yview)
    unique_scrollbar.pack(side="right", fill="y")
    unique_box.configure(yscrollcommand=unique_scrollbar.set)

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

def check_spelling(text_area, result_box, unique_box, dictionary):
    """ Do spell-check and Show the results

    Keyword Arguments:
        Nothing
            
    Returns:
        Nothing
    """
    code = text_area.get("1.0", customtkinter.END)
    clean_code = remove_comments_and_docstrings(code)
    suggestions, unique_expressions = spell_check_code(clean_code, dictionary)

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
    """
    import re
    code = re.sub(r'("""[\s\S]*?"""|\'\'\'[\s\S]*?\'\'\')', '', code)
    code = re.sub(r'#.*', '', code)
    return code