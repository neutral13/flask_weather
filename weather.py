from dotenv import load_dotenv
import requests
import os

load_dotenv()


def get_current_weather(city="Dhaka"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    return weather_data
