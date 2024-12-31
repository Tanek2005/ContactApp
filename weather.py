import datetime as dt
import requests


API_KEY = "b0569eb04e9105312a931197d08be3f9"  
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"



city = str(input("Enter city"))


try:

    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    print(url)
    response = requests.get(url)
    

    if response.status_code == 200:
        data = response.json()
        weather = {

            'city': city.title(),
            'description': data['weather'][0]['description'].capitalize(),
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind_speed': data['wind']['speed']
        }
    print(f"{weather['city']} weather: Temp- {weather['temperature']} degrees,forecast : {weather['description']}")
    

        


except Exception as e:
    print(e)


