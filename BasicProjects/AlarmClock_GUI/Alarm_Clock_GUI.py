from tkinter import *
import datetime
import time
import winsound  # plays sounds on a windows platform


def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("The set date:{}".format(date))
        print(now)
        if now == set_alarm_timer:
            print("Time to Wake Up")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break


def actual_time():
    set_alarm_timer = f"{hour.get()}:{minute.get()}:{sec.get()}"
    print(set_alarm_timer)
    alarm(set_alarm_timer)


# GUI
root = Tk()
root.title("Alarm Clock")
root.geometry("450x100")

# Labels
time_format = Label(root, text="Enter time in 24 hour format!!", fg="red", bg="blue")
add_time = Label(root, text="Hour Min Sec")
set_your_alarm = Label(root, text="Set the time:")


# Variables
hour = StringVar()
minute = StringVar()
sec = StringVar()

hour_entry = Entry(root, textvariable=hour)
minute_entry = Entry(root, textvariable=minute)
sec_entry = Entry(root, textvariable=sec)


btn = Button(root, text="Set Alarm", command=actual_time)


add_time.grid(row=0, column=1, columnspan=3)
set_your_alarm.grid(row=1, column=0)
hour_entry.grid(row=1, column=1)
minute_entry.grid(row=1, column=2)
sec_entry.grid(row=1, column=3)
btn.grid(row=2, column=2)
time_format.grid(row=3, column=1, columnspan=3)
root.mainloop()