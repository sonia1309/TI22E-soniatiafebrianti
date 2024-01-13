import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import math

class CalculatorApp:
    def __init__(self, master):
        self.master = master
        master.title("Kalkulator Bangun Ruang")

        self.label = tk.Label(root, text="Pilih Bangun Ruang:")
        self.label.pack(padx=100, pady=20)

        self.options = ["Kubus", "Balok", "Limas Segiempat", "Prisma Segitiga", "Limas Segitiga", "Tabung", "Kerucut", "Bola"]
        self.selected_option = tk.StringVar()
        self.selected_option.set(self.options[0])

        self.option_menu = tk.OptionMenu(root, self.selected_option, *self.options)
        self.option_menu.pack(padx=100, pady=10)

        self.calculate_button = tk.Button(root, text="Hitung", command=self.calculate, bg="#A7E30E")
        self.calculate_button.pack(padx=100, pady=10) 

    def calculate(self):
        selected_shape = self.selected_option.get()

        if selected_shape == "Kubus":
            self.calculate_kubus()
        elif selected_shape == "Balok":
            self.calculate_balok()
        elif selected_shape == "Limas Segiempat":
            self.calculate_limas_segiempat()
        elif selected_shape == "Prisma Segitiga":
            self.calculate_prisma_segitiga()
        elif selected_shape == "Limas Segitiga":
            self.calculate_limas_segitiga()
        elif selected_shape == "Tabung":
            self.calculate_tabung()
        elif selected_shape == "Kerucut":
            self.calculate_kerucut()
        elif selected_shape == "Bola":
            self.calculate_bola()
        else:
            messagebox.showinfo("Peringatan", "Pilih bangun ruang yang valid.")

    def calculate_kubus(self):
        panjang_sisi = float(self.get_user_input("Masukkan panjang sisi:"))
        luas = 6 * panjang_sisi**2
        volume = panjang_sisi**3
        self.show_result(luas, volume)

    def calculate_balok(self):
        panjang = float(self.get_user_input("Masukkan panjang:"))
        lebar = float(self.get_user_input("Masukkan lebar:"))
        tinggi = float(self.get_user_input("Masukkan tinggi:"))
        luas = 2 * (panjang * (lebar + tinggi) + lebar * tinggi)
        volume = panjang * lebar * tinggi
        self.show_result(luas, volume)

    def calculate_limas_segiempat(self):
        panjang_sisi = float(self.get_user_input("Masukkan panjang sisi:"))
        tinggi = float(self.get_user_input("Masukkan tinggi:"))
        lebar = float(self.get_user_input("Masukkan lebar:"))
        luas = panjang_sisi**2 + 2 * panjang_sisi * math.sqrt((lebar/2)**2 + tinggi**2) + 2 * lebar * tinggi
        volume = (panjang_sisi**2 * tinggi) / 3
        self.show_result(luas, volume)

    def calculate_prisma_segitiga(self):
        panjang_sisi = float(self.get_user_input("Masukkan panjang sisi:"))
        lebar = float(self.get_user_input("Masukkan lebar:"))
        tinggi = float(self.get_user_input("Masukkan tinggi:"))
        luas = panjang_sisi * lebar + 2 * (0.5 * panjang_sisi * tinggi + 0.5 * lebar * tinggi)
        volume = (0.5 * panjang_sisi * lebar * tinggi)
        self.show_result(luas, volume)

    def calculate_limas_segitiga(self):
        panjang_sisi = float(self.get_user_input("Masukkan panjang sisi:"))
        lebar = float(self.get_user_input("Masukkan lebar:"))
        tinggi = float(self.get_user_input("Masukkan tinggi:"))
        luas = panjang_sisi**2 + 3 * (panjang_sisi * math.sqrt((lebar/2)**2 + tinggi**2))
        volume = (panjang_sisi**2 * tinggi) / 3
        self.show_result(luas, volume)

    def calculate_tabung(self):
        jari_jari = float(self.get_user_input("Masukkan panjang jari-jari:"))
        tinggi = float(self.get_user_input("Masukkan tinggi:"))
        luas = 2 * math.pi * jari_jari * (jari_jari + tinggi)
        volume = math.pi * jari_jari**2 * tinggi
        self.show_result(luas, volume)

    def calculate_kerucut(self):
        jari_jari = float(self.get_user_input("Masukkan panjang jari-jari:"))
        tinggi = float(self.get_user_input("Masukkan tinggi:"))
        luas = math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari**2 + tinggi**2))
        volume = (math.pi * jari_jari**2 * tinggi) / 3
        self.show_result(luas, volume)

    def calculate_bola(self):
        jari_jari = float(self.get_user_input("Masukkan panjang jari-jari:"))
        luas = 4 * math.pi * jari_jari**2
        volume = (4/3) * math.pi * jari_jari**3
        self.show_result(luas, volume)

    def get_user_input(self, message):
        return simpledialog.askfloat("Input", message)

    def show_result(self, luas, volume):
        messagebox.showinfo("Hasil Perhitungan", f"Luas: {luas}\nVolume: {volume}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()



