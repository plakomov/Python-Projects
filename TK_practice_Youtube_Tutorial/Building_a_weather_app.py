from tkinter import *
from PIL import ImageTk, Image
import requests  # package that allows to deal with urls
import json

root = Tk()
root.title("Weather App")
root.iconbitmap("./life_animal_squid_sea_octopus_icon_209493.ico")
root.geometry("300x100")

url_ = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=25&API_KEY=D4CA5491-E37E-4765-9C22-68854E0019EF"


def lookup():
    global zip_ent
    zp = zip_ent.get()
    try:  # We cover this in a try block so that we can safe guard it from errors
        url_ = "https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode="+zp +"&distance=25&API_KEY=D4CA5491-E37E-4765-9C22-68854E0019EF"
        api_request = requests.get(url_)
        api = json.loads(api_request.content)
        city = api[0]["ReportingArea"]
        aqi = api[0]["AQI"]
        airq = api[0]["Category"]["Name"]
        color = ""

        if airq == "Good":
            color = "green"
        elif airq == "Moderate":
            color = "yellow"
        elif airq == "Unhealthy for Sensitive Groups":
            color = "orange"
        elif airq == "Unhealthy":
            color = "red"
        elif airq == "Very Unhealthy":
            color = "#990066"
        elif airq == "Hazardous":
            color = "#660000"
        else:
            color == "white"

        myLabel = Label(root, text="City: {}  AQI: {}  Air Quality: {}".format(city, aqi, airq),
                        font=("TimesNewRoman", 10),
                        background=color)
        root.configure(background=color)
        myLabel.grid(row=0, column=0, columnspan=2)
    except Exception as e:
        api = "Error.."


zip_ent = Entry(root)
zip_ent.grid(row=1, column=0, sticky=(N,W,E,S))

btn = Button(root, text="Lookup Zipcode", command=lookup)
btn.grid(row=2, column=0, sticky=(N,W,E,S))



root.mainloop()
