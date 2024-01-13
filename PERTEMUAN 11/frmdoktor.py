import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from dokter import Dokter

class FormDokter:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # Label
        Label(mainFrame, text='NIP:').grid(row=0, column=0, sticky=W, padx=5, pady=5)
        self.txtNIP = Entry(mainFrame) 
        self.txtNIP.grid(row=0, column=1, padx=5, pady=5) 
        self.txtNIP.bind("<Return>",self.onCari) # menambahkan event Enter key

        Label(mainFrame, text='Nama:').grid(row=1, column=0, sticky=W, padx=5, pady=5)
        self.txtNama = Entry(mainFrame) 
        self.txtNama.grid(row=1, column=1, padx=5, pady=5) 

        Label(mainFrame, text='Jenis Kelamin:').grid(row=2, column=0, sticky=W, padx=5, pady=5)
        self.txtJK = StringVar()
        self.L = Radiobutton(mainFrame, text='Laki-laki', value='L', variable=self.txtJK)
        self.L.grid(row=2, column=1, padx=5, pady=5, sticky=W)
        self.L.select() # set pilihan yg pertama
        self.P = Radiobutton(mainFrame, text='Perempuan', value='P', variable=self.txtJK)
        self.P.grid(row=3, column=1, padx=5, pady=5, sticky=W)
        self.L.select() # set pilihan yg kedua 

        Label(mainFrame, text='Spesialis:').grid(row=4, column=0, sticky=W, padx=5, pady=5)
        self.txtSpesialis = Entry(mainFrame) 
        self.txtSpesialis.grid(row=4, column=1, padx=5, pady=5)

        Label(mainFrame, text='Tempat Bertugas:').grid(row=5, column=0, sticky=W, padx=5, pady=5)
        self.txtTempat_Bertugas = Entry(mainFrame) 
        self.txtTempat_Bertugas.grid(row=5, column=1, padx=5, pady=5)   
        
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)

        # define columns
        columns = ('id', 'nip', 'nama','jk', 'spesialis', 'tempat bertugas')

        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="30")
        self.tree.heading('nip', text='NIP')
        self.tree.column('nip', width="60")
        self.tree.heading('nama', text='Nama')
        self.tree.column('nama', width="200")
        self.tree.heading('jk', text='JK')
        self.tree.column('jk', width="30")
        self.tree.heading('spesialis', text='Spesialis')
        self.tree.column('spesialis', width="200")
        self.tree.heading('tempat bertugas', text='Tempat Bertugas')
        self.tree.column('tempat bertugas', width="200")
        
        # set tree position
        self.tree.place(x=0, y=200)
        self.onReload()
        
    def onClear(self, event=None):
        self.txtNIP.delete(0,END)
        self.txtNIP.insert(END,"")
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,"")
        self.txtSpesialis.delete(0,END)
        self.txtSpesialis.insert(END,"")
        self.txtTempat_Bertugas.delete(0,END)
        self.txtTempat_Bertugas.insert(END,"")       
        self.btnSimpan.config(text="Simpan")
        self.L.select()
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data dokter
        Dok = Dokter()
        result = Dok.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        Kesehatan=[]
        for row_data in result:
            Kesehatan.append(row_data)

        for Kesehatan in Kesehatan:
            self.tree.insert('',END, values=Kesehatan)
    
    def onCari(self, event=None):
        nip = self.txtNIP.get()
        Dok = Dokter()
        res = Dok.getByNIP(nip)
        rec = Dok.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Ditemukan")
            self.TampilkanData()
            self.ditemukan = True
        else:
            messagebox.showwarning("showwarning", "Data Tidak Ditemukan") 
            self.ditemukan = False
            self.txtNama.focus()
        return res
        
    def TampilkanData(self, event=None):
        nip = self.txtNIP.get()
        Dok = Dokter()
        res = Dok.getByNIP(Dok)
        self.txtNama.delete(0,END)
        self.txtNama.insert(END,Dok.nama)
        jk = Dok.jk
        if(jk=="P"):
            self.P.select()
        else:
            self.L.select()  
        self.txtSpesialis.delete(0,END)
        self.txtSpesialis.insert(END,Dok.spesialis)
        self.txtTempat_Bertugas.delete(0,END)
        self.txtTempat_Bertugas.insert(END,Dok.tempat_bertugas)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        nip = self.txtNIP.get()
        nama = self.txtNama.get()
        jk = self.txtJK.get()
        spesialis = self.txtSpesialis.get()
        tempat_bertugas = self.txtTempat_Bertugas.get()
        
        Dok = Dokter()
        Dok.nip = nip
        Dok.nama = nama
        Dok.jk = jk
        Dok.spesialis = spesialis
        Dok.tempat_bertugas = tempat_bertugas
        if(self.ditemukan==True):
            res = Dok.updateByNIP(nip)
            ket = 'Diperbarui'
        else:
            res = Dok.simpan()
            ket = 'Disimpan'
            
        rec = Dok.affected
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil "+ket)
        else:
            messagebox.showwarning("showwarning", "Data Gagal "+ket)
        self.onClear()
        return rec

    def onDelete(self, event=None):
        nip = self.txtNIP.get()
        nama = self.txtNama.get()
        jk = self.txtJK.get()
        spesialis = self.txtSpesialis.get()
        tempat_bertugas = self.txtTempat_Bertugas.get()
    
        Dok = Dokter()
        Dok.nip = nip
        Dok.nama = nama
        Dok.jk = jk
        Dok.spesialis = spesialis
        Dok.tempat_bertugas = tempat_bertugas
        if(self.ditemukan==True):
            res = Dok.deleteByNIP(nip)
            rec = Dok.affected
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            rec = 0
        
        if(rec>0):
            messagebox.showinfo("showinfo", "Data Berhasil dihapus")
        
        self.onClear()
    
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormDokter(root, "Aplikasi Data Dokter")
    root.mainloop() 