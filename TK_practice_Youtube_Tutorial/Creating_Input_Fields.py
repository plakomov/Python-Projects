from tkinter import *

root = Tk()

e = Entry(root, width=50, fg="green", bg="blue", borderwidth=5)
# e.get() method returns whatever has been inputted into the entry by the user
e.insert(0, "Enter your name:  ")  # inserts a string into the entry before the user has input anything into it


def myClick():
    myLabel = Label(root, text=e.get())
    myLabel.grid()


# We can use state input to disable the button by using the DISABLED option
myButton = Button(root, text="Enter your Name", command=myClick, fg="blue", bg="red")
myButton.grid()
e.grid()

root.mainloop()
