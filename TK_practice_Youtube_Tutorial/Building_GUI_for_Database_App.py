from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# We are going to use SQL Lite which comes with python

root = Tk()
root.title("Adding Databases")
root.iconbitmap("./life_animal_squid_sea_octopus_icon_209493.ico")
root.geometry("400x600")

# Database

# Create a database or connect to a database
conn = sqlite3.connect("address_book.db") # Connects to a specific database
# Creating a cursor instance
c = conn.cursor()

# Create table columns and rows
# This needs to run only once
# c.execute(""" CREATE TABLE addresses (
#         first_name text,
#         last_name text,
#         address text,
#         city text,
#         state text,
#         zipcode integer
#     )""")

# Functions

def update():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    record_id = delete_.get()
    c.execute(""" UPDATE addresses SET 
        first_name = :first,
        last_name = :last,
        address = :address,
        city = :city,
        state = :state,
        zipcode = :zipcode  
        
        WHERE oid = :oid """,
        {'first': f_name_editor.get(),
         'last': l_name_editor.get(),
         'address': address_editor.get(),
         'city': city_editor.get(),
         'state': state_editor.get(),
         'zipcode': zip_editor.get(),
         'oid': record_id})

    conn.commit()
    conn.close()
    editor.destroy()


def edit():
    global editor
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    editor = Toplevel()
    editor.title("Update a record")
    editor.iconbitmap("./life_animal_squid_sea_octopus_icon_209493.ico")
    editor.geometry("400x600")

    global f_name_editor
    global l_name_editor
    global address_editor
    global city_editor
    global state_editor
    global zip_editor

    # Creating Text Boxes
    f_name_editor = Entry(editor, width=30)
    f_name_editor.grid(row=0, column=1, padx=20, pady=(10, 0))

    l_name_editor = Entry(editor, width=30)
    l_name_editor.grid(row=1, column=1, padx=20)

    address_editor = Entry(editor, width=30)
    address_editor.grid(row=2, column=1, padx=20)

    city_editor = Entry(editor, width=30)
    city_editor.grid(row=3, column=1, padx=20)

    state_editor = Entry(editor, width=30)
    state_editor.grid(row=4, column=1, padx=20)

    zip_editor = Entry(editor, width=30)
    zip_editor.grid(row=5, column=1, padx=20)

    # Creating Box Labels
    f_name_label_e = Label(editor, text="First Name")
    f_name_label_e.grid(row=0, column=0, pady=(10, 0))

    l_name_label_e = Label(editor, text="Last Name")
    l_name_label_e.grid(row=1, column=0)

    address_label_e = Label(editor, text="Address")
    address_label_e.grid(row=2, column=0)

    city_label_e = Label(editor, text="City")
    city_label_e.grid(row=3, column=0)

    state_label_e = Label(editor, text="State")
    state_label_e.grid(row=4, column=0)

    zip_label_e = Label(editor, text="Zipcode")
    zip_label_e.grid(row=5, column=0)

    # Save record
    edit_btn = Button(editor, text="Save record", command=update)
    edit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

    record_id = delete_.get()
    c.execute("SELECT * FROM addresses WHERE oid = " + record_id)
    records = c.fetchall()  # fetches all of the records

    for element in records:
        f_name_editor.insert(0, element[0])
        l_name_editor.insert(0, element[1])
        address_editor.insert(0, element[2])
        city_editor.insert(0, element[3])
        state_editor.insert(0, element[4])
        zip_editor.insert(0, element[5])


    conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()

    # Delete a record
    c.execute("DELETE from addresses WHERE oid = " + delete_.get())

    delete_.delete(0, END)

    conn.commit()
    conn.close()


def submit():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    # Insert into table
    c.execute("INSERT INTO addresses VALUES (:f_name, :l_name, :address, :city, :state, :zipcode)",
              {
                'f_name': f_name.get(),
                'l_name': l_name.get(),
                'address': address.get(),
                'city': city.get(),
                'state': state.get(),
                'zipcode': zip_.get()
              })
    conn.commit()
    conn.close()
    # Clear the textboxes
    f_name.delete(0, END)
    l_name.delete(0, END)
    address.delete(0, END)
    city.delete(0, END)
    state.delete(0, END)
    zip_.delete(0, END)


def query():
    conn = sqlite3.connect("address_book.db")
    c = conn.cursor()
    # Query the database
    c.execute("SELECT *, oid FROM addresses")
    records = c.fetchall()  # fetches all of the records

    record = ""
    for member in records:
        record += str(member[0]) + " " + str(member[1]) + " " + "\t" + "ID " + str(member[6]) + "\n"

    query_label = Label(root, text=record)
    query_label.grid(row=11, column=0, columnspan=2)

    conn.commit()
    conn.close()


# Creating Text Boxes
f_name = Entry(root, width=30)
f_name.grid(row=0, column=1, padx=20, pady=(10, 0))

l_name = Entry(root, width=30)
l_name.grid(row=1, column=1, padx=20)

address = Entry(root, width=30)
address.grid(row=2, column=1, padx=20)

city = Entry(root, width=30)
city.grid(row=3, column=1, padx=20)

state = Entry(root, width=30)
state.grid(row=4, column=1, padx=20)

zip_ = Entry(root, width=30)
zip_.grid(row=5, column=1, padx=20)

delete_ = Entry(root, width=30)
delete_.grid(row=8, column=1, padx=20)


# Creating Box Labels
f_name_label = Label(root, text="First Name")
f_name_label.grid(row=0, column=0, pady=(10, 0))

l_name_label = Label(root, text="Last Name")
l_name_label.grid(row=1, column=0)

address_label = Label(root, text="Address")
address_label.grid(row=2, column=0)

city_label = Label(root, text="City")
city_label.grid(row=3, column=0)

state_label = Label(root, text="State")
state_label.grid(row=4, column=0)

zip_label = Label(root, text="Zipcode")
zip_label.grid(row=5, column=0)

delete_label = Label(root, text="Select ID Number")
delete_label.grid(row=8, column=0)

# Create a submit button
submit_btn = Button(root, text="Add record to the Database", command=submit)
submit_btn.grid(row=6, column=0, columnspan=2, padx=10, pady=10, ipadx=100)

# Create a Query Button
query_btn = Button(root, text="Show Records", command=query)
query_btn.grid(row=7, column=0, columnspan=2, padx=10, pady=10, ipadx=135)

# Create a Delete Button
delete_btn = Button(root, text="Delete Record", command=delete)
delete_btn.grid(row=9, column=0, columnspan=2, padx=10, pady=10, ipadx=136)

# Create an update button
update_btn = Button(root, text="Edit Record", command=edit)
update_btn.grid(row=10, column=0, columnspan=2, padx=10, pady=10, ipadx=143)


# Whenever a change happens to the database we want to commit the database
# Commit changes
conn.commit()

# Close connection
conn.close()


root.mainloop()