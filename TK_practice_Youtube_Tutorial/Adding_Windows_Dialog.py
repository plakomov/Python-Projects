from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Root")
root.iconbitmap("./life_animal_squid_sea_octopus_icon_209493.ico")

my_img = ImageTk.PhotoImage(Image.open("./Image_Folder/pg0.png"))


def open_():
    top = Toplevel()  # basically creates another windows widget
    top.title("Top Level")
    top.iconbitmap("./life_animal_squid_sea_octopus_icon_209493.ico")
    myLabel = Label(top, text="Top Window", image=my_img)
    myLabel.grid(row=1, column=0)
    btn = Button(top, text="Open another window", command=open_)  # Basically keeps reopening the same window over n'
    # over
    btn.grid(row=0, column=0)


b = Button(root, text="Open Top Level Window", command=open_)
b.grid()

root.mainloop()