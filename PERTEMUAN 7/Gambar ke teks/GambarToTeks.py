import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
from tesseract import tesseract


class TextExtractorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text Extractor App")

        # Define path to tesseract.exe
        self.path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Initialize path_to_image as None
        self.path_to_image = None

        # Point tessaract_cmd to tessaract.exe
        pytesseract.tesseract_cmd = self.path_to_tesseract

        # Create UI elements
        self.create_widgets()

    def create_widgets(self):
        # Display the author information
        author_label = tk.Label(self.root, text="Aplikasi Extract Gambar ke Teks")
        author_label.grid(row=0, column=0, padx=10, pady=10)

        # Button to choose image file
        choose_file_button = tk.Button(self.root, text="Pilih Gambar", command=self.choose_image)
        choose_file_button.grid(row=1, column=0, padx=10, pady=10)

        try:
            if self.path_to_image:
                # Open image with PIL
                img = Image.open(self.path_to_image)

                # Extract text from image
                text = pytesseract.image_to_string(img)

                # Display the image in the Tkinter window
                img.thumbnail((300, 300))
                img_tk = ImageTk.PhotoImage(img)
                image_label = tk.Label(self.root, image=img_tk)
                image_label.image = img_tk
                image_label.grid(row=2, column=0, padx=10, pady=10)

                # Display extracted text
                text_label = tk.Label(self.root, text=f"Extracted Text:\n{text}")
                text_label.grid(row=3, column=0, padx=10, pady=10)

        except FileNotFoundError:
            error_label = tk.Label(self.root, text=f"File not found: {self.path_to_image}")
            error_label.grid(row=2, column=0, padx=10, pady=10)
        except Exception as e:
            error_label = tk.Label(self.root, text=f"Error: {str(e)}")
            error_label.grid(row=2, column=0, padx=10, pady=10)

    def choose_image(self):
        self.path_to_image = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        self.create_widgets()

if __name__ == "__main__":
    root = tk.Tk()
    app = TextExtractorApp(root)
    root.mainloop()
