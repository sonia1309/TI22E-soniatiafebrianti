import tkinter as tk
from tkinter import messagebox

def save_jadwal_kuliah():
    jadwal_data = entry_jadwal.get()
    with open("jadwal_kuliah.txt", "a") as file:
        file.write(jadwal_data + "\n")
    entry_jadwal.delete(0, "end")
    messagebox.showinfo("Sukses", "Jadwal berhasil disimpan!")

def load_jadwal():
    try:
        with open("jadwal_kuliah.txt", "r") as file:
            jadwal_list = file.readlines()
            jadwal_text.config(state="normal")
            jadwal_text.delete(1.0, "end")
            for jadwal in jadwal_list:
                jadwal_text.insert("end", jadwal)
            jadwal_text.config(state="disabled")
    except FileNotFoundError:
        messagebox.showinfo("Info", "Tidak ada jadwal yang tersimpan.")

app = tk.Tk()
app.title("jadwal kuliah sonia tria febrianti ")

# Membuat label
label_nama = tk.Label(app, text="sonia tria febrianti")
label_nama.pack(pady=10)

label_jadwal = tk.Label(app, text="Masukkan Jadwal Kuliah:")
label_jadwal.pack()

entry_jadwal = tk.Entry(app, width=40)
entry_jadwal.pack()

save_button = tk.Button(app, text="Simpan Jadwal", command=save_jadwal_kuliah)
save_button.pack(pady=10)

load_button = tk.Button(app, text="Muat Jadwal", command=load_jadwal)
load_button.pack(pady=10)

jadwal_text = tk.Text(app, height=10, width=30)
jadwal_text.config(state="disable")
jadwal_text.pack()

app.mainloop()