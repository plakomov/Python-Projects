from tkinter import *
from PIL import ImageTk, Image  # <-- modules that allows to work and import images

root = Tk()
root.title("Icons_Images_Exit_Buttons")
root.iconbitmap("C:/Users/Pavlo Lakomov/Desktop/Excel Projects/Python "
                "Projects/Beginner/TK_practice_Youtube_Tutorial/life_animal_squid_sea_octopus_icon_209493.ico")
# Icon -- .ico file or png file

# Constants
num = 0

# Images
my_img_0 = ImageTk.PhotoImage(Image.open("./Image_Folder/pg0.png"))
my_img_1 = ImageTk.PhotoImage(Image.open("./Image_Folder/pg1.png"))
my_img_2 = ImageTk.PhotoImage(Image.open("./Image_Folder/pg2.png"))
my_img_3 = ImageTk.PhotoImage(Image.open("./Image_Folder/pg3.png"))
my_img_4 = ImageTk.PhotoImage(Image.open("./Image_Folder/pg4.png"))
my_img_5 = ImageTk.PhotoImage(Image.open("./Image_Folder/pg5.png"))

images_list = [my_img_0, my_img_1, my_img_2, my_img_3, my_img_4, my_img_5]

myLabel = Label(root, image=my_img_0)  # create a widget that is going to store the png file


def forward():
    global myLabel
    global num
    myLabel.grid_forget()
    if num == 4:
        myLabel.configure(image=images_list[num])
    else:
        num += 1
        myLabel.configure(image=images_list[num])
    myLabel.grid(row=1, column=0, columnspan=3)


def back():
    global num
    global myLabel
    myLabel.grid_forget()
    if num == 0:
        myLabel.configure(image=images_list[num])
    else:
        num -= 1
        myLabel.configure(image=images_list[num])
    myLabel.grid(row=1, column=0, columnspan=3)


button_quit = Button(root, text="Exit Program", command=root.quit)  # setting up an exit button
button_forward = Button(root, text=">>", command=forward)
button_backward = Button(root, text="<<", command=back)

myLabel.grid(row=1, column=0, columnspan=3)
button_quit.grid(row=0, column=1)
button_forward.grid(row=0, column=2)
button_backward.grid(row=0, column=0)

root.mainloop()
