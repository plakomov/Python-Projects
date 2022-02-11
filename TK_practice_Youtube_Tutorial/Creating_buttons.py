from tkinter import *

root = Tk()


def myClick():
    myLabel = Label(root, text="Look I clicked the button")
    myLabel.grid()


# We can use state input to disable the button by using the DISABLED option
myButton = Button(root, text="Click me!", padx=50, pady=50, command=myClick, fg="blue", bg ="red")
myButton.grid()

root.mainloop()
