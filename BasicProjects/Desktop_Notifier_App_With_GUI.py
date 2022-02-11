from plyer import notification
from tkinter import *
import winsound
import time

root = Tk()
root.title("Desktop Notifier App")
root.iconbitmap("./life_animal_squid_sea_octopus_icon_209493.ico")

# Variables
loop_number = IntVar()
loop_number.set(3)


def notify_me_():
    i = 0
    while i < loop_number.get():
        pop_notification()
        time.sleep(0.5 + int(entry_seconds.get()))
        i += 1


def pop_notification():
    title = entry_title.get()
    message = entry_message.get()
    sec = entry_seconds.get()
    notification.notify(
        title=title,
        message=message,
        app_icon="./life_animal_squid_sea_octopus_icon_209493.ico",
        timeout=int(sec))
    winsound.PlaySound("sound.wav", winsound.SND_ASYNC)


# Labels:
title_label = Label(root, text="Enter title: ")
message_label = Label(root, text="Enter message: ")
seconds_label = Label(root, text="Enter seconds for notification to loop: ")
title_label.grid(row=0, column=0, sticky=(E, W))
message_label.grid(row=1, column=0, sticky=(E, W))
seconds_label.grid(row=2, column=0, sticky=(E, W))

# Entries
entry_title = Entry(root)
entry_message = Entry(root)
entry_seconds = Entry(root)
entry_title.grid(row=0, column=1, sticky=(E, W))
entry_message.grid(row=1, column=1, sticky=(E, W))
entry_seconds.grid(row=2, column=1, sticky=(E, W))

# Radio Buttons
r_button = Radiobutton(root, text="1 Loop", variable=loop_number, value=1)
r2_button = Radiobutton(root, text="2 Loop", variable=loop_number, value=2)
r3_button = Radiobutton(root, text="3 Loop", variable=loop_number, value=3)

r_button.grid(row=0, column=2)
r2_button.grid(row=1, column=2)
r3_button.grid(row=2, column=2)

# Button
btn = Button(root, text="Notify me", command=notify_me_)
btn.grid(row=3, column=1)
root.mainloop()
