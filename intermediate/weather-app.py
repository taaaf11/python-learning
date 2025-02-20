import requests
import json

API_KEY = "c7a7e4e1fd2f4a5b85b5e5d0acafd57e"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city_name):
    URL = f"{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric"

    response = requests.get(URL)
    data = response.json()

    print(json.dumps(data, indent=4))

    if data.get("cod") != "404":
        main = data.get("main", {})
        weather = data.get("weather", [{}])[0]

        if main:
            temperature = main.get("temp", "N/A")
            pressure = main.get("pressure", "N/A")
            humidity = main.get("humidity", "N/A")
        else:
            temperature = pressure = humidity = "N/A"

        weather_description = weather.get("description", "No description available")

        print(f"Weather in {city_name}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Description: {weather_description.capitalize()}")
    else:
        print("City not found or invalid response from API.")

city_name = input("Enter your city name for its weather: ")

if city_name:
    get_weather(city_name)
else:
    print("Please enter a valid city name.")
