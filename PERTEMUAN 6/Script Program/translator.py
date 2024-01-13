import tkinter as tk
from googletrans import Translator

class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        # Entry for user input
        self.input_label = tk.Label(root, text="Enter text:")
        self.input_label.pack(pady=10)
        self.input_entry = tk.Entry(root, width=40)
        self.input_entry.pack(pady=10)

        # Button to perform translation
        self.translate_button = tk.Button(root, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=10)

        # Label to display translated text
        self.output_label = tk.Label(root, text="")
        self.output_label.pack(pady=10)

    def translate_text(self):
        # Get text from entry
        input_text = self.input_entry.get()

        # Translate text
        translator = Translator()
        translation = translator.translate(input_text, dest='sundanese')  # Change 'en' to the desired language code
        translated_text = translation.text

        # Update output label
        self.output_label.config(text=f"Translated text: {translated_text}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslator(root)
    root.mainloop()
