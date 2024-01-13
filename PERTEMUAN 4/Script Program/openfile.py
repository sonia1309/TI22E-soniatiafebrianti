from tkinter import *
from tkinter import filedialog

def file_open():
    textarea.delete('1.0',END)
    path=filedialog.askopenfilename(initialdir='D://file')
    fh=open(path,'r')
    read=fh.read()
    textarea.insert(END,read)

window =Tk()
window.geometry("600x600")

button = Button(window,text="Open File",command=file_open,font=("Times New Roman",15))
button.pack(pady=50)
textarea=Text(window)
textarea.pack(pady=20)

window.mainloop()