import os
from tkinter import Tk, Button, Label, filedialog
import pygame

class MP3Player:
    def __init__(self, master):
        self.master = master
        self.master.title("MP3 Player")
        self.master.geometry("300x150")
        
        # Label untuk menampilkan nama file MP3 yang dipilih
        self.label = Label(master, text="Spotify ala-ala",font=("Helvetica", 16))
        self.label.pack(pady=10,padx=5)

        # Tombol untuk memilih folder dan memainkan MP3
        self.select_button = Button(master, text="Pilih Folder", command=self.select_folder)
        self.select_button.pack()
        self.label.pack(pady=10,padx=5)

        self.play_button = Button(master, text="Mainkan MP3", command=self.play_music)
        self.play_button.pack()
        self.label.pack(pady=10,padx=5)

        # Inisialisasi Pygame mixer
        pygame.mixer.init()

    def select_folder(self):
        folder_path = filedialog.askdirectory()
        self.label.config(text=f"Folder MP3: {folder_path}")
        self.folder_path = folder_path

    def play_music(self):
        try:
            # Ambil semua file MP3 di folder
            mp3_files = [f for f in os.listdir(self.folder_path) if f.endswith(".mp3")]

            # Pilih file MP3 pertama
            mp3_file = os.path.join(self.folder_path, mp3_files[0])

            # Muat dan mainkan file MP3
            pygame.mixer.music.load(mp3_file)
            pygame.mixer.music.play()
            self.label.config(text=f"Sedang memainkan: {mp3_file}")
        except Exception as e:
            self.label.config(text="Error: " + str(e))


if __name__ == "__main__":
    root = Tk()
    mp3_player = MP3Player(root)
    root.mainloop()
