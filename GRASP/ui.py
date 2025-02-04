import tkinter as tk
from tkinter import filedialog
from GRASP.core import spell_check_code

def spell_check_ui(dictionary):
    """GUIの設定と実行"""
    root = tk.Tk()
    root.title("スペルチェッカー")

    text_area = tk.Text(root, wrap="word", height=15, width=50)
    text_area.pack(pady=10)

    def check_spelling():
        code = text_area.get("1.0", tk.END)
        errors = spell_check_code(code, dictionary)
        result_text = "\n".join(f"'{word}' → '{suggestion}'" for word, suggestion in errors.items())
        result_label.config(text=result_text if result_text else "No spelling errors found.")

    check_button = tk.Button(root, text="スペルチェック", command=check_spelling)
    check_button.pack(pady=5)

    result_label = tk.Label(root, text="", justify="left")
    result_label.pack(pady=5)

    root.mainloop()
