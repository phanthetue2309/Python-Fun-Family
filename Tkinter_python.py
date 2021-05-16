from tkinter import *
from tkinter import messagebox

def truyen():
    messagebox.showinfo('xinchao','khoekhong')

tk = Tk()

btn = Button(tk, text = 'click here',command = truyen)
btn.pack()
