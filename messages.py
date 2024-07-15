from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title("Message Box Tutorial")

def popup():
    #showinfo, showwarning, showerror, askquestion, asktocancel, askyesno
    response = messagebox.askyesno("This is my popup", "Hello world")
    #Label(root, text=response).pack()
    if response == 1:
        Label(root, text="You clicked yes!").pack()
    else:
        Label(root, text="You clicked no.").pack()

Button(root, text="Popup", command=popup).pack()

root.mainloop()