import requests
from pprint import pprint
import json


api_weather_url = f'https://api.openweathermap.org/data/2.5/weather?lat=55.751244&lon=37.618423&appid=594156179360808d788f634d8738d7a8'

weather_data = requests.get(api_weather_url).content
weather_data = json.loads(weather_data)

temp = round(float(weather_data['main']['temp']) - 273, 2)
pressure = weather_data['main']['pressure']
humidity = weather_data['main']['humidity']
max_temp = round(float(weather_data['main']['temp_max']) - 273, 2)
min_temp = round(float(weather_data['main']['temp_min']) - 273, 2)
wind_speed = round(float(weather_data['wind']['speed']), 2)

weather_text = f'Погода на сегодня:\n'
weather_text += f'  Температура: {temp}°С\n'
weather_text += f'  Температура(макс): {max_temp}°С\n'
weather_text += f'  Температура(мин): {min_temp}°С\n'
weather_text += f'  Давление: {pressure}мм рт.ст.\n'
weather_text += f'  Влажность: {humidity}\n'
weather_text += f'  Скорость ветра: {wind_speed}м/с\n'

print(weather_text)
