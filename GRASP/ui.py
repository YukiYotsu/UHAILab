import customtkinter
import tkinter as tk
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
    root.title("Spell Checker")
    root.geometry("600x400")
    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("blue")

    text_area = customtkinter.CTkTextbox(root, height=150, width=500, wrap ="word")
    text_area.pack(pady = 10, padx = 10)

    result_box = customtkinter.CTkTextbox(root, height = 100, width = 500, wrap = "word", state = "disabled")
    result_box.pack(pady = 10, padx = 10)

    def check_spelling():
        """ Do spell-check and Show the results

        Args:
            Nothing
            
        Returns:
            Nothing
        """
        code = text_area.get("1.0", "end").strip()
        errors = spell_check_code(code, dictionary)
        result_box.configure(state = "normal")
        result_box.delete("1.0", "end")

        if errors:
            result_text = "\n".join(f"'{word}' → '{suggestion}'" for word, suggestion in errors.items())
            result_box.insert("end", result_text)
        else:
            result_box.insert("end", "Perfectly-spelled!")

        result_box.configure(state="disabled")

    check_button = customtkinter.CTkButton(root, text="Check", command=check_spelling)
    check_button.pack(pady = 10)

    root.mainloop()
