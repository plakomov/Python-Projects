from tkinter import *
from tkinter import ttk

root = Tk()

content = ttk.Frame(root)
frame = ttk.Frame(content, borderwidth=5, relief="ridge", width=200, height=100)
namelbl = ttk.Label(content, text="Name")
name = ttk.Entry(content)

onevar = BooleanVar(value=True)
twovar = BooleanVar(value=False)
threevar = BooleanVar(value=True)

one = ttk.Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = ttk.Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = ttk.Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = ttk.Button(content, text="Okay")
cancel = ttk.Button(content, text="Cancel")

content.grid(column=0, row=0, sticky=(N, S, E, W))  # sticky makes the widget stick to a side
frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))
namelbl.grid(column=3, row=0, columnspan=2, sticky=(N, W), padx =5) # padx padding on the left and write
name.grid(column=3, row=1, columnspan=2, sticky=(N,E,W), pady=5, padx=5)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)


# Configuring how the columns/rows should resize

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
content.columnconfigure(0, weight=3)
content.columnconfigure(1, weight=3)
content.columnconfigure(2, weight=3)
content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)
content.rowconfigure(1, weight=1)


root.mainloop()
#
# >>> content.grid_slaves()  <-- tells use all the widgets gridded inside the master widget
# [<tkinter.ttk.Button object .!frame.!button2>, <tkinter.ttk.Button object .!frame.!button>,
# <tkinter.ttk.Checkbutton object .!frame.!checkbutton3>, <tkinter.ttk.Checkbutton object .!frame.!checkbutton2>,
# <tkinter.ttk.Checkbutton object .!frame.!checkbutton>, <tkinter.ttk.Entry object .!frame.!entry>,
# <tkinter.ttk.Label object .!frame.!label>, <tkinter.ttk.Frame object .!frame.!frame>]
# >>> for w in content.grid_slaves(): print(w)   # doing the same but for the columns and rows independently
# ...
# .!frame.!button2
# .!frame.!button
# .!frame.!checkbutton3
# .!frame.!checkbutton2
# .!frame.!checkbutton
# .!frame.!entry
# .!frame.!label
# .!frame.!frame
# >>> for w in content.grid_slaves(row=3): print(w)
# ...
# .!frame.!button2
# .!frame.!button
# .!frame.!checkbutton3
# .!frame.!checkbutton2
# .!frame.!checkbutton
# >>> for w in content.grid_slaves(column=0): print(w)
# ...
# .!frame.!checkbutton
# .!frame.!frame
# >>> namelbl.grid_info() # info will return a list of all grid options for the widget and its options
# {'in': <tkinter.ttk.Frame object .!frame>, 'column': 3, 'row': 0, 'columnspan': 2, 'rowspan': 1,
# 'ipadx': 0, 'ipady': 0, 'padx': 5, 'pady': 0, 'sticky': 'nw'}
# >>> namelbl.grid_configure(sticky=(E,W))   <-- configure lets you change one or more options on a widget
# >>> namelbl.grid_info()
# {'in': <tkinter.ttk.Frame object .!frame>, 'column': 3, 'row': 0, 'columnspan': 2, 'rowspan': 1,
# 'ipadx': 0, 'ipady': 0, 'padx': 5, 'pady': 0, 'sticky': 'ew'}