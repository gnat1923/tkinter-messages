from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Window Tutorial")

def open():
    top = Toplevel()
    top.title("Top Window")
    lbl =Label(top, text="Hello world").pack()
    btn2 = Button(top, text="Close Window", command=top.destroy).pack()

btn = Button(root, text="Open second window", command=open).pack()

#top = Toplevel()
#top.title("Top Window")
#lbl =Label(top, text="Hello world").pack()

root.mainloop()