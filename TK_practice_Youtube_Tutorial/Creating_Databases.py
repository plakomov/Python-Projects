from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# We are going to use SQL Lite which comes with python

root = Tk()
root.title("Adding Databases")
root.iconbitmap("./life_animal_squid_sea_octopus_icon_209493.ico")

# Database

# Create a database or connect to a database
conn = sqlite3.connect("address_book.db") # Connects to a specific database

# Creating a cursor instance
c = conn.cursor()

# Create table columns and rows
# This needs to run only once
c.execute(""" CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
    )""")

# Whenever a change happens to the database we want to commit the database
# Commit changes
conn.commit()

# Close connection
conn.close()


root.mainloop()