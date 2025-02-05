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
    root.geometry("600x600")
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
    result_label = customtkinter.CTkLabel(root, text="", justify="left", wraplength=500)
    result_label.pack(pady=5)

    # area for unique expressions
    customtkinter.CTkLabel(root, text="🐧 Unique Expressions:", anchor="w").pack(pady=(10, 0))
    unique_box = customtkinter.CTkTextbox(root, height=100, width=500, wrap="word", state="disabled")
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

def check_spelling(text_area, result_label, unique_box, dictionary):
    """ Do spell-check and Show the results

    Keyword Arguments:
        Nothing
            
    Returns:
        Nothing
    """
    code = text_area.get("1.0", customtkinter.END)
    suggestions, unique_expressions = spell_check_code(code, dictionary)

    # show misspelled candidates
    result_text = "\n".join(f"'{word}' → '{suggestion}'" for word, suggestion in suggestions.items())
    result_label.configure(text=result_text if result_text else "✅ No spelling errors found.")

    # show unique expressions
    unique_text = "\n".join(f"'{word}'" for word in unique_expressions)
    unique_box.configure(state="normal")
    unique_box.delete("1.0", customtkinter.END)
    unique_box.insert(customtkinter.END, unique_text if unique_text else "🚀 No unique expressions found.")
    unique_box.configure(state="disabled")