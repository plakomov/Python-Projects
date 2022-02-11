from tkinter import * # standard binding to Tk (* means we imported everything)
from tkinter import ttk # newer themed widgets

def calculate(*args):
    try:
        value = float(feet.get()) # feet is the StringVar() below
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass

root = Tk()   # Setting up the main application and giving it a title
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")   # Creates a frame widget that contains the context of our user interface
mainframe.grid(column=0, row=0, sticky=(N, W, E, S)) # grid it places directly inside the main application window
root.columnconfigure(0, weight=1) # tell it to fill anyspace if the window is resized
root.rowconfigure(0, weight=1)

# Need two things to create a widget; the widget itself and where to place it;
# Need to specify its parent, a widget in which the new widget will be placed in
feet = StringVar()
#                         |
#                         <  parent widget
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))  # Tells us where to put the widget inside the other widget
# Sticky means to anchor the widget to a side of the widget


meters = StringVar() # StringVar() is a must; it's required for the TK textvariable
#                            |
#                            <  TK will automatically update the global variable feet because of textvariable
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)  # Adds padding to each of the child widgets

feet_entry.focus()  #tells Tk to focus on the entry widget
root.bind("<Return>", calculate) # tells Tk that if the use presses Enter button, then it should call the calculate met

root.mainloop()  # telling Tk to enter its event loop, which is necessary for everything to appear onscreen and allow
# users to interact with it
