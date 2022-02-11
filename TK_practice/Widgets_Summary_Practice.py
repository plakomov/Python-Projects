from tkinter import *
from tkinter import ttk

root = Tk()
frame =  ttk.Frame("parent")

# The size of the frame is determined by the widgets within it; however, can be explicitly determined by the height
# and by the weight attributes


#Padding
frame['padding'] = 5           # 5 pixels on all sides
frame['padding'] = (5,10)      # 5 on left and right, 10 on top and bottom
frame['padding'] = (5,7,10,12) # left: 5, top: 7, right: 10, bottom: 12

#Borderwidth

frame['borderwidth'] = 2
frame['relief'] = 'sunken'  # relief specifies the visual appearence of the border


# Style of the frame example

s = ttk.Style()
s.configure('Danger.TFrame', background='red', borderwidth=5, relief='raised')
ttk.Frame(root, width=200, height=200, style='Danger.TFrame').grid()

# Label widget

label = ttk.Label("parent", Text = "Full name")

# One can change the what text is displayed by modifying this configuration
resultsContents = StringVar()
label['textvariable'] = resultsContents
resultsContents.set('New value to display')

# Tkinter only allows you to attach widgets to an instance of the StringVar class but not arbitrary Python variables.
# This class contains all the logic to watch for changes and communicate them back and forth between the variable and
# Tk. Use the get and set methods to read or write the current value of the variable.

# You can also use Labels to display images as well
image = PhotoImage(file='myimage.gif')
label['image'] = image

# Labels can also display both an image and text at the same time. You'll often see this in toolbar buttons. To do
# so, use the compound configuration option. The default value is none, meaning display only the image if present; if
# there is no image, display the text specified by the text or textvariable options. Other possible values for the
# compound option are text (text only), image (image only), center (text in the center of image), top (image above
# text), left, bottom, and right.

# Button Widget

# button = ttk.Button("parent", text='Okay', command=submitForm)

# default configuration -- active (tells the user that this button is default button;Default buttons are invoked if
# users hit the Return or Enter key)

# command configuration connect's the buttons actions and its applications

action = ttk.Button(root, text="Action", default="active", command=myaction)
root.bind('<Return>', lambda e: action.invoke())

# Button states can disable or enabled

b.state(['disabled'])          # set the disabled flag
b.state(['!disabled'])         # clear the disabled flag
b.instate(['disabled'])        # true if disabled, else false
b.instate(['!disabled'])       # true if not disabled, else false
b.instate(['!disabled'], cmd)  # execute 'cmd' if not disabled

# Checkbutton

# Example
measureSystem = StringVar()
check = ttk.Checkbutton(parent, text='Use Metric',
	    command=metricChanged, variable=measureSystem,
	    onvalue='metric', offvalue='imperial')

# Unlike regular buttons, checkbuttons also hold a value. We've seen how the textvariable option links the label of a
# widget to a variable. The variable option for checkbuttons behaves similarly, except it links a variable to the
# widget's current value. The variable is updated whenever the widget is toggled. By default, checkbuttons use a
# value of 1 when checked and 0 when not checked. These can be changed to something else using the onvalue and
# offvalue options.

# Radiobutton

phone = StringVar()
home = ttk.Radiobutton(parent, text='Home', variable=phone, value='home')
office = ttk.Radiobutton(parent, text='Office', variable=phone, value='office')
cell = ttk.Radiobutton(parent, text='Mobile', variable=phone, value='cell')

# Entry

# You can also get or change the value of the entry widget without going through the linked variable. The get method
# returns the current value, and the delete and insert methods let you change the contents, e.g.

print('current value is %s' % name.get())
name.delete(0,'end')          # delete between two indices, 0-based
name.insert(0, 'your name')   # insert new text at a given index

# Passwords in Entry
# Entries can be used for passwords, where the actual contents are displayed as a bullet or other
# symbol. To do this, set the show configuration option to the character you'd like to display.

passwd = ttk.Entry(parent, textvariable=password, show="*")

# Validation for Entry
# We can restrict what the user can or cannot write in the entry by validating the string

# The validation criteria are specified via an entry's validatecommand configuration option. You supply a piece of
# code whose job is to validate the entry. It functions like a widget callback or event binding, except that it
# returns a value (whether or not the entry is valid). We'll validate the entry on every keystroke; this is specified
# by providing a value of key to the validate configuration option.

import re
def check_num(newval):
    return re.match('^[0-9]*$', newval) is not None and len(newval) <= 5
check_num_wrapper = (root.register(check_num), '%P')

num = StringVar()
e = ttk.Entry(root, textvariable=num, validate='key', validatecommand=check_num_wrapper)
e.grid(column=0, row=0, sticky='we')

# Example of validation of zip code plus setting an errormessage

errmsg = StringVar()
formatmsg = "Zip should be ##### or #####-####"

def check_zip(newval, op):
    errmsg.set('')
    valid = re.match('^[0-9]{5}(\-[0-9]{4})?$', newval) is not None
    btn.state(['!disabled'] if valid else ['disabled'])
    if op=='key':
        ok_so_far = re.match('^[0-9\-]*$', newval) is not None and len(newval) <= 10
        if not ok_so_far:
            errmsg.set(formatmsg)
        return ok_so_far
    elif op=='focusout':
        if not valid:
            errmsg.set(formatmsg)
    return valid
check_zip_wrapper = (root.register(check_zip), '%P', '%V')

zip = StringVar()
f = ttk.Frame(root)
f.grid(column=0, row=0)
ttk.Label(f, text='Name:').grid(column=0, row=0, padx=5, pady=5)
ttk.Entry(f).grid(column=1, row=0, padx=5, pady=5)
ttk.Label(f, text='Zip:').grid(column=0, row=1, padx=5, pady=5)
e = ttk.Entry(f, textvariable=zip, validate='all', validatecommand=check_zip_wrapper)
e.grid(column=1, row=1, padx=5, pady=5)
btn = ttk.Button(f, text="Process")
btn.grid(column=2, row=1, padx=5, pady=5)
btn.state(['disabled'])
msg = ttk.Label(f, font='TkSmallCaptionFont', foreground='red', textvariable=errmsg)
msg.grid(column=1, row=2, padx=5, pady=5, sticky='w')


# Important to notice the validate command to the entry  "all"  <- arranges for the validcommnad callback to
# be invoked on not only keystrokes but other triggers as well; the trigger is passed to the callback using the
# %V percent substitution; The callback differentiated between key and focusout triggers (you can also check for
# focusin )

# %P is the new value of the entry if the validation passes


# Other percent substitutions allow you to get the entry's contents prior to editing (%s), differentiate between
# insert and delete (%d), where an insert or delete occurs (%i), what is being inserted or deleted (%S), the current
# setting of the validate option (%v) and the name of the widget (%W).

# Combobox

countryvar = StringVar()
country = ttk.Combobox(parent, textvariable=countryvar)