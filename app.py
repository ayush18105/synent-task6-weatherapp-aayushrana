import requests

def get_weather(city):
    try:
        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            print("❌ Unable to fetch weather data.")
            return

        data = response.json()

        current = data["current_condition"][0]

        temperature = current["temp_C"]
        humidity = current["humidity"]
        wind_speed = current["windspeedKmph"]
        description = current["weatherDesc"][0]["value"]

        print("\n" + "=" * 40)
        print("🌤 WEATHER REPORT")
        print("=" * 40)
        print(f"📍 City        : {city.title()}")
        print(f"🌡 Temperature : {temperature} °C")
        print(f"💧 Humidity    : {humidity}%")
        print(f"🌬 Wind Speed  : {wind_speed} km/h")
        print(f"☁ Condition   : {description}")
        print("=" * 40)

        # Save report
        with open("weather_history.txt", "a") as file:
            file.write(
                f"{city.title()} | {temperature}°C | {humidity}% | {description}\n"
            )

    except requests.exceptions.ConnectionError:
        print("❌ Internet connection error.")

    except requests.exceptions.Timeout:
        print("❌ Request timed out.")

    except Exception as e:
        print("❌ Error:", e)


print("=" * 40)
print("🌦 Welcome to WeatherWise")
print("=" * 40)

while True:
    city = input("\nEnter City Name: ")

    if city.strip() == "":
        print("❌ Please enter a city name.")
        continue

    get_weather(city)

    choice = input("\nCheck another city? (y/n): ")

    if choice.lower() != "y":
        print("\n👋 Thank you for using WeatherWise!")
        break