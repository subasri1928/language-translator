import tkinter as tk
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

# Available languages for dropdown
languages = {
    "English": "en",
    "Tamil": "ta",
    "Hindi": "hi",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Chinese": "zh-cn",
    "Japanese": "ja"
}

# Translate function
def translate_text():
    try:
        src_text = text_input.get("1.0", tk.END).strip()
        target_lang = languages[lang_var.get()]
        
        if not src_text:
            messagebox.showwarning("Warning", "Please enter some text!")
            return

        translated = GoogleTranslator(source='auto', target=target_lang).translate(src_text)
        text_output.delete("1.0", tk.END)
        text_output.insert(tk.END, translated)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI Window
root = tk.Tk()
root.title("?? Language Translator")
root.geometry("600x400")
root.resizable(False, False)

# Input label & box
tk.Label(root, text="Enter Text:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
text_input = tk.Text(root, height=5, width=70, font=("Arial", 11))
text_input.pack(padx=10)

# Language dropdown
tk.Label(root, text="Translate To:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
lang_var = tk.StringVar(value="Tamil")
lang_menu = ttk.Combobox(root, textvariable=lang_var, values=list(languages.keys()), state="readonly", font=("Arial", 11))
lang_menu.pack(padx=10, pady=5)

# Translate button
tk.Button(root, text="Translate", command=translate_text, font=("Arial", 12), bg="lightblue").pack(pady=10)

# Output box
tk.Label(root, text="Translated Text:", font=("Arial", 12)).pack(anchor="w", padx=10, pady=5)
text_output = tk.Text(root, height=5, width=70, font=("Arial", 11))
text_output.pack(padx=10)

# Run GUI
root.mainloop()
