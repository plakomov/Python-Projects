from tkinter import *
from tkinter import ttk
root = Tk()
# create a button, passing two options:
button = ttk.Button(root, text="Hello", command="buttonpressed")
button.grid()
# check the current value of the text option:
button['text']
# 'Hello'
# change the value of the text option:
button['text'] = 'goodbye'
# another way to do the same thing:
button.configure(text='goodbye')
# check the current value of the text option:
button['text']
#'goodbye'
# get all information about the text option:
button.configure('text')
# ('text', 'text', 'Text', '', 'goodbye')
# get information on all options for this widget:
button.configure()
#{'cursor': ('cursor', 'cursor', 'Cursor', '', ''), 'style': ('style', 'style', 'Style', '', ''),
#'default': ('default', 'default', 'Default', <index object at 0x00DFFD10>, <index object at 0x00DFFD10>),
#'text': ('text', 'text', 'Text', '', 'goodbye'), 'image': ('image', 'image', 'Image', '', ''),
#'class': ('class', '', '', '', ''), 'padding': ('padding', 'padding', 'Pad', '', ''),
#'width': ('width', 'width', 'Width', '', ''),
#'state': ('state', 'state', 'State', <index object at 0x0167FA20>, <index object at 0x0167FA20>),
#'command': ('command', 'command' , 'Command', '', 'buttonpressed'),
#'textvariable': ('textvariable', 'textVariable', 'Variable', '', ''),
#'compound': ('compound', 'compound', 'Compound', <index object at 0x0167FA08>, <index object at 0x0167FA08>),
#'underline': ('underline', 'underline', 'Underline', -1, -1),
#'takefocus': ('takefocus', 'takeFocus', 'TakeFocus', '', 'ttk::takefocus')}


# Main idea: to get the methods of a specific widget run the configure method on the widget


def print_hierarchy(w, depth=0):
    print('  '*depth + w.winfo_class() + ' w=' + str(w.winfo_width()) + ' h=' + str(w.winfo_height()) + ' x=' + str(w.winfo_x()) + ' y=' + str(w.winfo_y()))
    for i in w.winfo_children():
        print_hierarchy(i, depth+1)

print_hierarchy(root)

# The method above loops through the children_widget of a widget returning some basic info about the widgets using the winfo command