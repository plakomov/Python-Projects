from tkinter import *
from tkinter import messagebox
import base64 as bm


# Need to always create a root widget

root = Tk()
root.title("Encoding and Decoding String Messages")
root.iconbitmap("C:/Users/Pavlo Lakomov/Desktop/Excel Projects/Python "
                "Projects/Beginner/TK_practice_Youtube_Tutorial/life_animal_squid_sea_octopus_icon_209493.ico")

# Variables
r = IntVar()
r.set("1")

#messagebox.showinfo("Important Information", "You must encrypt the text before decrypting")

# Functions


def encrypt(text):
    bits = text.encode("ascii")
    return bm.b64encode(bits)


def decrypt(text):
    return bm.b64decode(text)


def update(number):
    if number == 0:
        b.configure(text="Decode")
    else:
        b.configure(text="Encode")
    b.grid(row=1, column=1, sticky=W+E)


def crypt():
    global r
    if e.get() == "":
        messagebox.showinfo("No string", "Please a enter text to encrypt/decrypt")
    text = e.get()
    e.delete(0,END)
    if r.get() == 1:
        text = encrypt(text)
        e.insert(0, text)
    else:
        text = decrypt(text)
        e.insert(0, text)


# Entry
e = Entry(root, text="Enter your string here", width=50)
e.insert(0, "Enter text here: ")


# RadioButtons
r1 = Radiobutton(root, text="Encode", variable=r, value=1, command=lambda: update(1))
r2 = Radiobutton(root, text="Decode", variable=r, value=0, command=lambda: update(0))

# Button
b = Button(root, text="Encode", command=crypt)

# Grid
e.grid(row=0, column=0, columnspan=3)
r1.grid(row=0, column=3, padx=10)
r2.grid(row=1, column=3, padx=10)
b.grid(row=1, column=1, sticky=W+E)

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)




root.mainloop()