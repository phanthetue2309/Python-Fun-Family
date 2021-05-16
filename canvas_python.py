from tkinter import *
from tkinter import messagebox

def truyen():
    messagebox.showinfo('xinchao','khoekhong')

tk = Tk()

cas = Canvas(tk, width = 1000 , height = 1000)
###for i in range(1000):
   ### cas.create_line(100,200,200, i )
cas.create_rectangle(100,200,500,500)
cas.create_text(200,300,text="Phan The Tue" ,font =('Times',19))
cas.pack()
