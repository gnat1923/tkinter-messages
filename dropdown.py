from tkinter import *


root = Tk()
root.title("Dropdown Tutorial")
root.geometry("400x400") # set initial size

def show():
    myLabel = Label(root, text=clicked.get()).pack()

options = [
            "Monday", 
            "Tuesday", 
            "Wednesday", 
            "Thursday", 
            "Friday"
            ]

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(root, clicked, *options) # Use the * when referencing a list
drop.pack()

myButton = Button(root, text="Show selection", command=show)
myButton.pack()

root.mainloop()