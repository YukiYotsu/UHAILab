import customtkinter
import tkinter as tk
import os
from tkinter import filedialog, simpledialog, messagebox
from GRASP.core import spell_check_code, save_user_defined_correction
from config import USER_DEFINED_CORRECTIONS_FILE_Path

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
    customtkinter.CTkLabel(root, text="🔤 Input Text:", anchor="w").pack(pady=(10, 0))
    
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

    check_button = customtkinter.CTkButton(button_frame, text="✅ Check Spelling", command=lambda: append_tag(text_area, result_box, dictionary))
    check_button.grid(row=0, column=1, padx=5)

    define_button = customtkinter.CTkButton(button_frame,text="📕 Define", command=lambda: define_correction(text_area))
    define_button.grid(row=0, column=2, padx=5)

    # area for candidates of correctly-spelled
    customtkinter.CTkLabel(root, text="🔍 Spelling Suggestions:", anchor="w").pack(pady=(10, 0))
    result_box = customtkinter.CTkTextbox(root, height=100, width=480, wrap="word", state="disabled")
    result_box.pack(pady=5, padx=10)

    root.mainloop()

def open_file(text_area):
    """ Open a file and display its contents

    Keyword Arguments:
        program_path: the path indicating the place of the program file (e.g. .py file) 
                    to be spell-checked
    
    Returns:
        Nothing
    """
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]) # especially only .py file
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete("1.0", customtkinter.END)
            text_area.insert(customtkinter.END, file.read())

def recommend_correction(misspelled_word):
    """ Ask the user for a correction and save it
    """
    correct_word = simpledialog.askstring("Correction", f"Enter the correct spelling for '{misspelled_word}':")
    if correct_word:
        save_user_defined_correction(misspelled_word, correct_word)

def append_tag(text_area, result_box, dictionary):
    """ Do spell-check and Append tags

    Keyword Arguments:
        Nothing
            
    Returns:
        Nothing
    """
    text = text_area.get("1.0", customtkinter.END).strip()
    suggestions = spell_check_code(text, dictionary)

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
    result_box.configure(state="normal")
    result_box.delete("1.0", customtkinter.END)

    for word, suggestion in suggestions.items():
        result_box.insert(customtkinter.END, f"'{word}' → '{suggestion}'\n")
        if suggestion == "❓UNIQUE":
            recommend_correction(word)

    result_box.configure(state="disabled")

def define_correction(text_area):
    """ Allow user to define a correction for selected text
    """
    try:
        selected_text = text_area.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
    except tk.TclError:
        messagebox.showwarning("No Selection", "Please select a misspelled word first.")
        return

    if not selected_text:
        messagebox.showwarning("No Selection", "Please select a misspelled word first.")
        return

    correct_word = simpledialog.askstring("Define Correction", f"Enter the correct spelling for '{selected_text}':")
    if correct_word:
        save_user_defined_correction(selected_text, correct_word)
        messagebox.showinfo("Correction Saved", f"Correction for '{selected_text}' saved as '{correct_word}'.")
