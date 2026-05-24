from backend.tools.calculator_tool import calculate
from backend.tools.weather_tool import get_weather
from backend.tools.web_search_tool import web_search


def handle_tools(message):

    lower = message.lower()

    # Calculator
    if any(op in message for op in [
        "+",
        "-",
        "*",
        "/"
    ]):

        return calculate(message)

    # Weather
    if "weather" in lower:

        city = lower.replace(
            "weather in",
            ""
        ).strip()

        return get_weather(city)

    # Web Search
    if any(keyword in lower for keyword in [
        "latest",
        "news",
        "who is",
        "what is"
    ]):

        return web_search(message)

    return None