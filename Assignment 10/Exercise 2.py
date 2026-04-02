import requests


def get_weather_by_city():
    # 1. Configuration
    api_key = "04f751e080b34f5d323c8c1d7700106f"
    base_url = "https://api.openweathermap.org/data/2.5/weather"

    # 2. Ask the user for the city name
    city_name = input("Enter the name of a municipality: ")

    # 3. Construct the request URL
    # Note: We can add '&units=metric' to the URL to get Celsius directly,
    # but the assignment asks us to find out how to convert it manually.
    request_url = f"{base_url}?q={city_name}&appid={api_key}"

    try:
        response = requests.get(request_url)
        response.raise_for_status()

        # 4. Parse the data
        weather_data = response.json()

        # Extract description and temperature (in Kelvin)
        description = weather_data["weather"][0]["description"]
        temp_kelvin = weather_data["main"]["temp"]

        # 5. Convert Kelvin to Celsius
        temp_celsius = temp_kelvin - 273.15

        # 6. Print the results
        print(f"Weather condition: {description.capitalize()}")
        print(f"Temperature: {temp_celsius:.1f} °C")

    except requests.exceptions.RequestException:
        print("Could not retrieve weather data. Please check the city name.")


if __name__ == "__main__":
    get_weather_by_city()