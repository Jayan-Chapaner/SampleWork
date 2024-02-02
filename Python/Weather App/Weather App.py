''' The goal of this project is to create a weather app that shows the current weather conditions and forecast for a specific location.

    Here are the steps you can take to create this project:

    Use the requests library to make an API call to a weather service (e.g. OpenWeatherMap) to retrieve the weather data for a specific location.

    Use the json library to parse the JSON data returned by the API call.

    Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

    Use the Pillow library to display the weather icons.

    Use the datetime library to display the current time and date. '''

# Imports
import requests
import json
import tkinter as tk
from PIL import ImageTk as Pil_imageTk
import datetime

# Declare Resources and Initialise Window

img_dir = (r"C:\Users\jchap\Desktop\Life\KreativStorm\Assignments\Week 3\app images") # directory for styling
icon_dir = (r"C:\Users\jchap\Desktop\Life\KreativStorm\Assignments\Week 3\app images\Weather Icons") # directory for weather icons
apiKey = "72b36e10b11ccbfd51cd6e6d37c5a354"
kelvin = 273 # kelvin for temperature adjustments later

weatherApp = tk.Tk()
weatherApp.geometry("800x600") #size of the window by default
weatherApp.resizable(0,0) #to make the window size fixed
weatherApp.title("Weather App") # App Name
weatherApp.configure(bg="#57adff") # background of app

# Function to get current weather conditions
def getWeather(e):
    cityName = searchField.get() #get entered name

    # run query and populate list
    weatherQuery = 'http://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&APPID=' + apiKey
    
    weatherData = requests.get(weatherQuery).json()

    # if no error found populate GUI with data else report error
    if int(weatherData['cod']) == 200:
        lblTemp['text'] = "Current Temperatue : " + str(int(weatherData['main']['temp'] - kelvin)) + "°C"
        lblHumid['text'] = "Humidity : " + str(weatherData['main']['humidity']) + "%"
        lblPressure['text'] = "Pressure : " + str(weatherData['main']['pressure']) + "hPa"
        lblWindSpeed['text'] = "Wind Speed : " + str(round(weatherData['wind']['speed']* 3.6,2) )+"m/s"
        lblDesc['text'] = "Conditions : " + str(weatherData['weather'][0]['description'])
        lblclock["text"] = datetime.datetime.strftime(datetime.datetime.utcfromtimestamp(weatherData["dt"]+weatherData["timezone"]),"%d/%m/%Y %I:%M %p")

        getForcast(str(weatherData['coord']['lat']), str(weatherData['coord']['lon'])) #function call to get forcast

    else:
        lblclock["text"] = "Error Location Not Found"
        lblTemp['text'] = "Error Location Not Found"
        lblHumid['text'] = ""
        lblPressure['text'] = ""
        lblWindSpeed['text'] = ""
        lblDesc['text'] = ""

# Function to get future forcast
def getForcast(lat,lon):

    # run query and populate list
    forcastQuery = 'http://api.openweathermap.org/data/2.5/forecast?lat=' + lat + "&lon="+lon +'&appid=' + apiKey
    
    forcastData = requests.get(forcastQuery).json()

    # if no error found place icons and temperature in GUI
    if int(forcastData['cod']) == 200:
        iconDay1 = Pil_imageTk.PhotoImage(file=icon_dir+"\\"+str(forcastData['list'][0]['weather'][0]['icon'])+".png")
        imgDay1.config(image = iconDay1)
        imgDay1.image = iconDay1
        lblTempDay1['text'] = "Temperatue : " + str(int(forcastData['list'][0]['main']['temp'] - kelvin)) + "°C"

        iconDay2 = Pil_imageTk.PhotoImage(file=icon_dir+"\\"+str(forcastData['list'][1]['weather'][0]['icon'])+".png")
        imgDay2.config(image = iconDay2)
        imgDay2.image = iconDay2
        lblTempDay2['text'] = "Temperatue : " + str(int(forcastData['list'][1]['main']['temp'] - kelvin)) + "°C"

        iconDay3 = Pil_imageTk.PhotoImage(file=icon_dir+"\\"+str(forcastData['list'][2]['weather'][0]['icon'])+".png")
        imgDay3.config(image = iconDay3)
        imgDay3.image = iconDay3
        lblTempDay3['text'] = "Temperatue : " + str(int(forcastData['list'][2]['main']['temp'] - kelvin)) + "°C"

        iconDay4 = Pil_imageTk.PhotoImage(file=icon_dir+"\\"+str(forcastData['list'][3]['weather'][0]['icon'])+".png")
        imgDay4.config(image = iconDay4)
        imgDay4.image = iconDay4
        lblTempDay4['text'] = "Temperatue : " + str(int(forcastData['list'][3]['main']['temp'] - kelvin)) + "°C"

        iconDay5 = Pil_imageTk.PhotoImage(file=icon_dir+"\\"+str(forcastData['list'][4]['weather'][0]['icon'])+".png")
        imgDay5.config(image = iconDay5)
        imgDay5.image = iconDay5
        lblTempDay5['text'] = "Temperatue : " + str(int(forcastData['list'][4]['main']['temp'] - kelvin)) + "°C"
    else:
        lblclock["text"] = "Error getting data"




# GUI 

# Set date and time and place label
lblclock = tk.Label(weatherApp,text="",font=("*",30),fg="white",bg="#57adff")
lblclock["text"] = datetime.datetime.strftime(datetime.datetime.now(),"%d/%m/%Y %I:%M %p")
lblclock.place(x=200,y=20)


# Search bar creaation and functionality
searchBar = tk.PhotoImage(file=img_dir+"\searchBar.png")
tk.Label(weatherApp, image=searchBar, bg="#57adff").place(x=200,y=100)

cloudLogo = tk.PhotoImage(file=img_dir+"\searchLogo.png")
tk.Label(weatherApp, image=cloudLogo,bg="#041c2c").place(x=206,y=107)

searchIcon = tk.PhotoImage(file=img_dir+"\searchIcon.png")
searchButton = tk.Button(weatherApp, image=searchIcon,bg="#041c2c",relief=tk.FLAT)
searchButton.place(x=550,y=107)
searchButton.bind('<Button-1>', getWeather) # bind the button press to run function to get weathers

searchField = tk.Entry(weatherApp,justify="center", insertbackground='white',width=16,font=("*",25),fg="white", bg="#041c2c",border=0)
searchField.place(x=260,y=110)


# display Window for weather data and background

dataBg = tk.PhotoImage(file=img_dir+"\dataBG.png")
tk.Label(weatherApp, image=dataBg, bg="#57adff").place(x=200,y=190)

lblTemp = tk.Label(weatherApp, text="Temperature",fg ="white",bg="#00bbff")
lblTemp.place(x=210,y=200)
lblHumid = tk.Label(weatherApp, text="Humidity",fg ="white",bg="#00bbff")
lblHumid.place(x=210,y=225)
lblPressure = tk.Label(weatherApp, text="Pressure",fg ="white",bg="#00bbff")
lblPressure.place(x=210,y=250)
lblWindSpeed = tk.Label(weatherApp, text="Wind Speed",fg ="white",bg="#00bbff")
lblWindSpeed.place(x=210,y=275)
lblDesc = tk.Label(weatherApp, text="Description",fg ="white",bg="#00bbff")
lblDesc.place(x=210,y=300)


# Forcast Display

#Function to get day names
def getDay(offset):

    return str(datetime.datetime.strftime(datetime.datetime.now()+datetime.timedelta(days = offset),"%A"))

# base border frame
frame = tk.LabelFrame(weatherApp, width=800, height=200,bg="#041c2c")
frame.pack(side=tk.BOTTOM)

frameboxL = tk.PhotoImage(file=img_dir+"\Lbox.png")

# Forcast Boxes
tk.Label(frame,image=frameboxL,bg="#041c2c").place(x=30,y=20)
frame1 = tk.Frame(weatherApp, width=120, height=140,bg="#00bbff")
frame1.place(x=34,y=424)
lblDay1 = tk.Label(weatherApp,text = getDay(1),fg ="white",bg="#00bbff")
lblDay1.place(x=35,y=425)
imgDay1 = tk.Label(frame1,fg ="white",bg="#00bbff")
imgDay1.place(x=1,y=25)
lblTempDay1 = tk.Label(weatherApp,text = "",fg ="white",bg="#00bbff")
lblTempDay1.place(x=35,y=540)



tk.Label(frame,image=frameboxL,bg="#041c2c").place(x=180,y=20)
frame2 = tk.Frame(weatherApp, width=120, height=140,bg="#00bbff")
frame2.place(x=184,y=424)
lblDay2 = tk.Label(weatherApp,text = getDay(2),fg ="white",bg="#00bbff")
lblDay2.place(x=184,y=425)
imgDay2 = tk.Label(frame2,fg ="white",bg="#00bbff")
imgDay2.place(x=1,y=25)
lblTempDay2 = tk.Label(weatherApp,text = "",fg ="white",bg="#00bbff")
lblTempDay2.place(x=184,y=540)


tk.Label(frame,image=frameboxL,bg="#041c2c").place(x=330,y=20)
frame3 = tk.Frame(weatherApp, width=120, height=140,bg="#00bbff")
frame3.place(x=334,y=424)
lblDay3 = tk.Label(weatherApp,text = getDay(3),fg ="white",bg="#00bbff")
lblDay3.place(x=335,y=425)
imgDay3 = tk.Label(frame3,fg ="white",bg="#00bbff")
imgDay3.place(x=1,y=25)
lblTempDay3 = tk.Label(weatherApp,text = "",fg ="white",bg="#00bbff")
lblTempDay3.place(x=335,y=540)


tk.Label(frame,image=frameboxL,bg="#041c2c").place(x=480,y=20)
frame4 = tk.Frame(weatherApp, width=120, height=140,bg="#00bbff")
frame4.place(x=484,y=424)
lblDay4 = tk.Label(weatherApp,text = getDay(4),fg ="white",bg="#00bbff")
lblDay4.place(x=485,y=425)
imgDay4 = tk.Label(frame4,fg ="white",bg="#00bbff")
imgDay4.place(x=1,y=25)
lblTempDay4 = tk.Label(weatherApp,text = "",fg ="white",bg="#00bbff")
lblTempDay4.place(x=485,y=540)

tk.Label(frame,image=frameboxL,bg="#041c2c").place(x=630,y=20)
frame5 = tk.Frame(weatherApp, width=120, height=140,bg="#00bbff")
frame5.place(x=634,y=424)
lblDay5 = tk.Label(weatherApp,text = getDay(5),fg ="white",bg="#00bbff")
lblDay5.place(x=635,y=425)
imgDay5 = tk.Label(frame5,fg ="white",bg="#00bbff")
imgDay5.place(x=1,y=25)
lblTempDay5 = tk.Label(weatherApp,text = "",fg ="white",bg="#00bbff")
lblTempDay5.place(x=635,y=540)

# Bind enter press to run getWeather function
weatherApp.bind('<Return>', getWeather)

# run app
weatherApp.mainloop()