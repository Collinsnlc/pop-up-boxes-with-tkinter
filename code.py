from tkinter import *
from tkinter import messagebox
root= Tk()

def popup():
    responce=messagebox.askyesno("this is my pop up","Hellow World!")
    l=Label(root,text=responce).pack()
    if responce == 1:
        l = Label(root, text="you said yes").pack()
    else:
        l = Label(root, text="you said no").pack()


b= Button(root,command=popup)
b.pack()

# All options for pop up box= showinfo, showwarning, showerror, askquestion, askokcancel, askyesno








mainloop()
