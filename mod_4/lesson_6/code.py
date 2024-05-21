import requests # подключаем библиотеку для отправки GET-запросов
from pprint import pprint
from datetime import datetime
# координаты населенного пункта в формате "широта, долгота"
coords = (55.041111, 82.934441)
API_KEY = "a8f6fef7a296bbce70aa16aca85698e3" # ВАШ ключ с доступом к OpenWeather API
# начальная часть GET-запроса к OpenWeather API
url = 'https://api.openweathermap.org/data/2.5/weather?'
params = {
    'lat': coords[0],
    'lon': coords[1],
    'appid': API_KEY,
    'units': 'metric',
    'lang': 'ru'
}
response = requests.get(url, params=params) 
data = response.json()
# pprint(data)
main = data['main']
description = data['weather'][0]['description']
wind = data['wind']
sunrise = data['sys']['sunrise']
sunset = data['sys']['sunset']
print(f"время: {(sunset-sunrise)//3600} часов {((sunset-sunrise)%3600)//60} минут")
print(f"Восход в {datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')}")
print(f"Закат в {datetime.fromtimestamp(sunset).strftime('%H:%M:%S')}")
print(f"Температура {main['temp']}°C, {description}")
print(f"Ощущается как {main['feels_like']}°C")
print(f"Ветер {wind['speed']} м/c")
print(f"Влажность {main['humidity']}%")