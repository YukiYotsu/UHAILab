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
    root = tk.Tk()
    root.title("Spell Checker")

    text_area = tk.Text(root, wrap="word", height=15, width=50)
    text_area.pack(pady=10)

    def check_spelling():
        """ Set the detail of spell-checker UI

        Args:
            Nothing
            
        Returns:
            Nothing
        """
        code = text_area.get("1.0", tk.END)
        errors = spell_check_code(code, dictionary)
        result_text = "\n".join(f"'{word}' → '{suggestion}'" for word, suggestion in errors.items())
        result_label.config(text=result_text if result_text else "No spelling errors found.")

    check_button = tk.Button(root, text="Check", command=check_spelling)
    check_button.pack(pady=5)

    result_label = tk.Label(root, text="", justify="left")
    result_label.pack(pady=5)

    root.mainloop()
