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
    root.geometry("600x500")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    text_area = customtkinter.CTkTextbox(root, height=200, width=500, wrap ="word")
    text_area.pack(pady = 10, padx = 10)

    result_box = customtkinter.CTkTextbox(root, height = 100, width = 500, wrap = "word", state = "disabled")
    result_box.pack(pady = 10, padx = 10)

    def open_file():
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

    def check_spelling():
        """ Do spell-check and Show the results

        Args:
            Nothing
            
        Returns:
            Nothing
        """
        code = text_area.get("1.0", customtkinter.END)
        errors = spell_check_code(code, dictionary)
        result_text = "\n".join(f"'{word}' → '{suggestion}'" for word, suggestion in errors.items())
        result_label.configure(text=result_text if result_text else "No spelling errors found.")

    open_button = customtkinter.CTkButton(root, text="Open Python File", command=open_file)
    open_button.pack(pady = 5)

    # The button for execute spell-check
    check_button = customtkinter.CTkButton(root, text="Check Spelling", command=check_spelling)
    check_button.pack(pady = 5)

    result_label = customtkinter.CTkLabel(root, text="", justify="left", wraplength=500)
    result_label.pack(pady = 10)

    root.mainloop()
