from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title("Adding Frames")
root.iconbitmap("./life_animal_squid_sea_octopus_icon_209493.ico")

frame = LabelFrame(root, text="Frame Test", padx=10, pady=10) # adding a frame ; pads the widgets inside from the border
frame.grid(padx=100, pady=100) # padding here pads the frame from the root

b = Button(frame, text="In the frame", command=root.quit)
b2 = Button(frame, text="Nothing", command=root.quit)
b.grid(row=0, column=0)
b2.grid(row=1, column=0)

root.mainloop()