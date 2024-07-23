from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Checkbox Tutorial")
root.geometry("400x400") # set initial size

def show():
    myLabel = Label(root, text=var.get()).pack()

# Create a tkinter variable
var = StringVar()

c = Checkbutton(root, text="Check this box", variable=var, onvalue="On", offvalue="Off")
c.deselect() # This prevents the strange default behaviour o a checkbox when not using binary values
c.pack()

myLabel = Label(root, text=var.get()).pack()

myButton = Button(root, text="Show selection", command=show).pack()

root.mainloop()