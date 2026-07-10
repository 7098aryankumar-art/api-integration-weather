import requests

city = input("Enter city name: ")

weather_url = f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(weather_url)

        weather_data = response.json()

        current = weather_data["current_condition"][0]

        print("\n----- Weather Details -----")
        print(f"City        : {city.title()}")
        print(f"Temperature : {current['temp_C']} °C")
        print(f"Humidity    : {current['humidity']}%")
        print(f"Condition   : {current['weatherDesc'][0]['value']}")
    else:
        print("Unable to get weather information.")

except Exception:
    print("Something went wrong. Please check your internet connection.")