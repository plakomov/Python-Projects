from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Slider tutorial")
root.iconbitmap("./life_animal_squid_sea_octopus_icon_209493.ico")
root.geometry("400x400") # lets designate the shape of the starting root window

var = StringVar()
var.set("ON")

def update():
    global c
    global label
    label.configure(text=var.get())
    label.pack()


c = Checkbutton(root, text="Checkbox test", variable=var, onvalue="ON", offvalue="OFF")
c.deselect()
c.pack()

label = Label(root, text=var.get())
label.pack()

b = Button(root, text="Update label", command=update)
b.pack()

root.mainloop()