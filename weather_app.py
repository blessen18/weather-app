import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")
URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    try:
        r = requests.get(URL, params=params, timeout=10)
        r.raise_for_status()
    except requests.exceptions.HTTPError:
        if r.status_code == 404:
            return None, "City not found."
        if r.status_code == 401:
            return None, "Invalid or not-yet-active API key."
        return None, f"Server error: {r.status_code}"
    except requests.exceptions.RequestException:
        return None, "Network problem. Check your internet."
    return r.json(), None

def show(data):
    print(f"\n{data['name']}, {data['sys']['country']}")
    print(f"Temp: {data['main']['temp']}°C "
          f"(feels like {data['main']['feels_like']}°C)")
    print(f"Condition: {data['weather'][0]['description'].title()}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind: {data['wind']['speed']} m/s\n")

def main():
    while True:
        city = input("Enter city (or 'q' to quit): ").strip()
        if city.lower() == "q":
            break
        if not city:
            continue
        data, error = get_weather(city)
        print(error) if error else show(data)

if __name__ == "__main__":
    main()