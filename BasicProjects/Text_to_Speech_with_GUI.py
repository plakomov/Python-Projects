from tkinter import *
import pyttsx3

root = Tk()
root.title("Text to speech GUI")
root.iconbitmap("life_animal_squid_sea_octopus_icon_209493.ico")


# Functions


def speak():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.say(text.get(1.0, END))
    engine.setProperty("rate", 50) # changes the rate
    engine.setProperty("voice", voices[1].id)  # 1 sets it to female, 0 sets it to male
    engine.runAndWait()


# Label
label_text = Label(root, text="Write something in the entry and convert it to speech automatically")
label_text.grid(row=0, column=0, sticky=(N, S))

# Text Widget
text = Text(root)
text.grid(row=0, column=1)

# Button
btn = Button(root, text="Speak Machine!", command=speak)
btn.grid(row=1, column=1, sticky=(W,E))


root.mainloop()