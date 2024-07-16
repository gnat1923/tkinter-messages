from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image

root = Tk()
root.title("Window Tutorial")

def open():
    global my_img
    root.filename = filedialog.askopenfilename(
                                            initialdir="C:/Users/ckenn/VS Studio/Python/tkinter/img/static/img", 
                                            title="Select a file", 
                                            filetypes=(("jpg files", "*.jpg"),("all files","*.*"))
                                            )

    my_label = Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_image_label = Label(image=my_img).pack()


my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()