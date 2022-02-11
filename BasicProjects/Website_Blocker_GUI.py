# A simple GUI program that will let the user block specified websites for a specific time
# Note: This python file MUST be run by the admin
# Modules
from tkinter import *
from datetime import datetime, timedelta

# Root window

root = Tk()
root.title("Website Blocker")
root.iconbitmap("life_animal_squid_sea_octopus_icon_209493.ico")

# Global Constants
redirect = "127.0.0.1"  # NEVER ALTER
# hosts_path = r"C:\Windows\System32\drivers\etc\hosts"  # links this to the addresses to be blocked; # NEVER ALTER
hosts_practice_path = r"./hosts_practice"
site_list = []  # List of sites to be blocked
default_time = datetime(2010, 1, 10)  # Will be used to unblock the sites
handler_ = IntVar()
handler_.set(1)


# Functions
def unblock(): # This function is not working properly
    """Unblocks all/specific websites the websites"""
    with open(hosts_practice_path, "r+") as hosts_files:
        if len(hosts_files.readlines()) < 22:
            websites.delete(1.0, END)
            websites.insert(1.0, "<<THERE ARE NO WEBSITES CURRENTLY ON THE BLOCK LIST>>")
        else:
            lines = hosts_files.readlines()
            hosts_files.seek(0)  # sets the pointer to the beginning of the file
            for line in lines:
                if not any(site in line for site in hosts_practice_path):
                    hosts_files.write(line)
            hosts_files.truncate()
    hosts_files.close()


def block():
    """Blocks all the lists specified in the list"""
    hours, minute, sec = int(hour_entry.get()), int(minute_entry.get()), int(seconds_entry.get())
    if check_time(hours, minute, sec):
        websites.delete(1.0, END)
        websites.insert(END, " ERROR: WRONG TIME SPECIFIED")
    else:
        fut = datetime.now() + timedelta(hours=hours, minutes=minute, seconds=sec)
        webs = websites.get(1.0, END).split("\n")
        webs.remove("")
        run_blocker(webs, fut)


def show():
    """Shows all the sites currently blocked"""
    with open(hosts_practice_path, "r+") as hosts_files:
        hosts_content = hosts_files.readlines()
        if len(hosts_content) < 22:
            websites.delete(1.0, END)
            websites.insert(1.0, "<<THERE ARE NO WEBSITES CURRENTLY ON THE BLOCK LIST>>")
        else:
            websites.delete(1.0, END)
            website_list = ""
            for i in range(21, len(hosts_content)):
                website_list = website_list + hosts_content[i] + "\n"
            websites.insert(1.0, website_list)
    hosts_files.close()


def update():
    if handler_.get() == 1:
        btn.configure(text="Block")
    else:
        btn.configure(text="Unblock")


def run_blocker(l_webs: list, date: datetime):
    if datetime.now() < date:
        print("block sites")
        with open(hosts_practice_path, "r+") as hosts_files:
            hosts_content = hosts_files.read()
            for site in l_webs:
                if site not in hosts_content:
                    hosts_files.write(redirect + " " + site + "\n")
        hosts_files.close()


def check_time(hour, minutes, seconds):
    if hour < 0 or hour > 24:
        return True
    if minutes < 0 or minutes > 60:
        return True
    if seconds < 0 or seconds > 24:
        return True
    return False


def alter():
    if handler_.get() == 1:
        block()
    else:
        unblock()


# Entries: Year, Month, Day, Hour, Minute, Seconds
hour_entry = Entry(root)
minute_entry = Entry(root)
seconds_entry = Entry(root)

# Labels
date_label = Label(root, text="Hour/Minutes/Seconds")
date_label_1 = Label(root, text="Enter Duration:")

# Check buttons
ch_btn = Checkbutton(root, text="Block/Unblock", variable=handler_, onvalue=1, offvalue=0, command=update)

# Button
btn = Button(root, text="Block", command=alter)
btn_2 = Button(root, text="Show", command=show)

# Entry
websites = Text(root)
websites.insert(1.0, "<<WRITE EACH WEBSITE ON A NEW LINE>>\n<<DELETE THIS BEFORE WRITING>>")

# Grid
date_label_1.grid(row=1, column=0)
date_label.grid(row=0, column=1, columnspan=3, sticky=(W, E))

ch_btn.grid(row=2, column=0)

btn.grid(row=3, column=1, columnspan=2, sticky=(W, E))
btn_2.grid(row=3, column=3, sticky=(W, E))

hour_entry.grid(row=1, column=1, sticky=(W, E))
minute_entry.grid(row=1, column=2, sticky=(W, E))
seconds_entry.grid(row=1, column=3, sticky=(W, E))

websites.grid(row=2, column=1, columnspan=3)

# Tests
hour_entry.insert(0, "9")
minute_entry.insert(0, "5")
seconds_entry.insert(0, "0")

# Run the GUI
root.mainloop()
