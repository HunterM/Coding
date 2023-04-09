#!/usr/bin/env python
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile

fileName = NONE

def newFile():
    global fileName
    fileName = "No name"
    text.delete('1.0', END)

def saveAs():
    out = asksaveasfile(mode='w', defaultextension='.csv')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror("Could not save")

def openFile():
    global fileName
    inp = askopenfile(mode='r')
    if inp is None:
        return 
        fileName = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', END)





root = Tk()
root.title("Note")
root.geometry("500x500")

text = Text(root, width=500, height=500)
text.pack()


menuBar = Menu(root)
fileMenu = Menu(menuBar)
menuBar.add_cascade(label="Файл", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label= "New", command=newFile)
fileMenu.add_command(label="Save", command=saveAs)



root.config(menu=menuBar)
root.mainloop()