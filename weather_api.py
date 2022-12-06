import requests

f = open("api.txt", "r")
API_KEY = f.read()
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city_name = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city_name}&units=metric&lang=bg"
get_response = requests.get(request_url)

if get_response.status_code == 200:    # this code(200) means that the request is successful, and we have a valid answer
    received_data = get_response.json()
    weather = received_data["weather"][0]["description"]
    temperature = received_data["main"]["temp"]
    feels_like = received_data["main"]["feels_like"]
    # min_temp = data["main"]["temp_min"]
    # max_temp = data["main"]["temp_max"]
    humidity = received_data["main"]["humidity"]
    wind = received_data["wind"]["speed"]
    city = received_data["name"]

    print(f"City: {city}")
    print(f"Weather: {weather}")
    print(f"Temperature: {temperature} °C")  # you can use chr(176) to display the Celsius symbol
    print(f"Feels like: {feels_like} °C")
    # print(f"Minimal temp.: {min_temp} °C")
    # print(f"Maximum temp.: {max_temp} °C")
    print(f"Humidity: {humidity} %")
    print(f"Wind speed: {wind} m/s")
else:
    print("An error occurred. Please check the city name or API key validity.")
