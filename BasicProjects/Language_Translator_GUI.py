from tkinter import *
from googletrans import Translator, LANGUAGES


# Intialize the window page

root = Tk()
root.title("Language Translator")
#root.iconbitmap("./life_animal_squid_sea_octopus_icon_209493")

# Variables
opt_1 = StringVar()
opt_2 = StringVar()
opt_1.set("en")
opt_2.set("uk")

# Functions


def translate_():
    output_text.delete(1.0, END)
    translator = Translator()
    out = translator.translate(input_text.get(1.0, END), dest=opt_2.get(), src=opt_1.get())
    output_text.insert(1.0, out.text)


def updateLabel(num):
    if num == 1:
        choice_label.configure(text=f"Chosen language is {LANGUAGES[opt_1.get()].capitalize()}")
    else:
        output_label.configure(text=f"Chosen language is {LANGUAGES[opt_2.get()].capitalize()}")


option1 = OptionMenu(root, opt_1, *LANGUAGES.keys(), command=lambda s: updateLabel(1))
option2 = OptionMenu(root, opt_2, *LANGUAGES.keys(), command=lambda s: updateLabel(2))
choice_label = Label(root, text=f"Input language is {LANGUAGES[opt_1.get()].capitalize()}")
output_label = Label(root, text=f"Ouput language is {LANGUAGES[opt_2.get()].capitalize()}")

# Text
input_text = Text(root)
input_text.grid(row=2, column=0)
output_text = Text(root)
output_text.grid(row=2, column=1)

# Button
btn = Button(root, text="Translate", command=translate_)
btn.grid(row=3, column=0, columnspan=2)

choice_label.grid(row=0, column=0, sticky=(E, W))
output_label.grid(row=0, column=1, sticky=(E, W))
option1.grid(row=1, column=0, sticky=(E, W))
option2.grid(row=1, column=1, sticky=(E, W))

root.mainloop()