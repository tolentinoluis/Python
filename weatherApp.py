import tkinter as tk
from PIL import Image
from PIL import ImageTk
import requests
from tkinter import font

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print("This is the entry:", entry)

#API KEY - a589eee492b9c83032795da5ec5a08c6
#API call - api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}
#api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}
def format_response(weather):
    try:
        name = weather['city']['name']
        desc = weather['list'][0]['weather'][0]['description']

        final_str = 'City: %s \nConditions: %s' %(name, desc)
    except:
        final_str = 'Error : There was a problem with GET info'

    #return str(name) + ' ' + str(desc)
    return final_str

def get_weather(city):
    weather_key = 'a589eee492b9c83032795da5ec5a08c6'
    url = 'https://api.openweathermap.org/data/2.5/forecast'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()

    #print(weather)
    print(weather['city']['name'])
    #print(weather['list'][0]['weather'][0]['description'])
    print(weather['list'][5])

    #label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH, bg='grey')
canvas.pack()

label = tk.Label(root, text='Luis Tolentino')
label.pack()

#background_image = ImageTk.PhotoImage(file='/Users/luistolentino/Documents/Miggy/Dev/python/GUI/landscape.png')
#background_label = tk.Label(root, image=background_image)
#background_label.place(relwidt= 1, relheight= 1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx = 0.5, rely = 0.1, relwidt = 0.75, relheight = 0.1, anchor='n')

entry = tk.Entry(frame, font=('Courier New',18))
entry.place( relwidt= 0.65, relheight= 1)

button = tk.Button(frame, text="Get Weather", font=12, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidt = 0.3, relheight= 1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx =0.5 , rely = 0.25, relwidt = 0.75, relheight = 0.6, anchor='n')

label = tk.Label(lower_frame, font=('Courier New',18))
label.place(relwidt= 1, relheight= 1)

root.mainloop()