import requests

API_KEY = "2e459643a7df6365797526099053b27a"


def get_weather(city):

    url = f"""
    https://api.openweathermap.org/data/2.5/weather
    ?q={city}
    &appid={API_KEY}
    &units=metric
    """

    response = requests.get(url)

    data = response.json()

    try:

        temp = data["main"]["temp"]

        desc = data["weather"][0]["description"]

        return f"{temp}°C, {desc}"

    except Exception:

        return "Weather not found"