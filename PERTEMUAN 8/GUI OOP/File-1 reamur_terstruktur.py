# File-1 (reamur_terstruktur.py)
class Reamur:
  def __init__(self, suhu):
    self.suhu = suhu

  def get_Reamur(self):
    val = self.suhu
    return val
    
  def get_fahrenheit(self):
    val = (9/4 * self.suhu) + 32
    return val
  
  def get_celcius(self):
    val = (5/4 * self.suhu) 
    return val
  
  def get_kelvin(self):
    val = 5/4 * self.suhu + 273
    return val

# File-2 (FrmReamur.py)
from tkinter import Frame,Label,Entry,Button,YES,BOTH,END,Tk,W

class FrmReamur:
    def __init__(self, parent, title):
        self.parent = parent       
        #self.parent.geometry("400x400")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.aturKomponen()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES) 
        Label(mainFrame, text='Reamur:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Fahrenheit:").grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Celcius:").grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text="Kelvin:").grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        
        self.txtReamur = Entry(mainFrame) 
        self.txtReamur.grid(row=0, column=1, padx=5, pady=5)  

        self.txtFahrenheit = Entry(mainFrame) 
        self.txtFahrenheit.grid(row=2, column=1, padx=5, pady=5) 

        self.txtcelcius = Entry(mainFrame) 
        self.txtcelcius.grid(row=3, column=1, padx=5, pady=5) 

        self.txtKelvin = Entry(mainFrame) 
        self.txtKelvin.grid(row=4, column=1, padx=5, pady=5) 

        self.btnHitung = Button(mainFrame, text='Hitung',
            command=self.onHitung)
        self.btnHitung.grid(row=1, column=1, padx=5, pady=5)
        
    def onHitung(self):
        R = Reamur(int(self.txtReamur.get()))

        # Suhu dalam Fahrenheit
        F = R.get_fahrenheit()
        self.txtFahrenheit.delete(0,END)
        self.txtFahrenheit.insert(END,str(F))

        # Suhu dalam Fahrenheit
        C = R.get_celcius()
        self.txtcelcius.delete(0,END)
        self.txtcelcius.insert(END,str(C))

        # Suhu dalam Fahrenheit
        K = R.get_kelvin()
        self.txtKelvin.delete(0,END)
        self.txtKelvin.insert(END,str(K))
               
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = Tk()  
    aplikasi = FrmReamur(root, "Program Konversi Suhu Reamur")
    root.mainloop() 