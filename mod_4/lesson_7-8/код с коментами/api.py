

import requests
from datetime import datetime

API_KEY = ''

# функция для получения координат указанного города
def get_coords(city_name):
    url = 'http://api.openweathermap.org/geo/1.0/direct?'
    params = {
        'q': city_name,
        'appid': API_KEY
    }
    response = requests.get(url, params=params)
    data = response.json()[0]
    return data['lat'], data['lon']

# функция для получения текущей погоды в указанном городе
def get_weather(city_name):
    coords = get_coords(city_name)
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
    main = data['main']
    description = data['weather'][0]['description']
    wind = data['wind']
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    return (f"Температура {main['temp']} °C, {description}",
            f"Ощущается как {main['feels_like']} °C",
            f"Влажность {main['humidity']} %",
            f"Ветер {wind['speed']} м/c",
            f"Восход в {datetime.fromtimestamp(sunrise).strftime('%H:%M:%S')}",
            f"Закат в {datetime.fromtimestamp(sunset).strftime('%H:%M:%S')}")

# функция для получения прогноза погоды на несколькой дней для указанного города
def get_daily_forecasts(city_name):
    # вызываем функцию get_coords() для получения координат города
    coords = get_coords(city_name)
    url = 'https://api.openweathermap.org/data/2.5/forecast?'
    params = {
        'lat': coords[0],
        'lon': coords[1],
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }
    response = requests.get(url, params=params)
    # получаем список с прогнозами погоды
    data = response.json()['list']
    # создаем словарь, где ключ - дата, значение - словарь с погодными данными (ключ - время, значение - погодные данные)
    forecasts = {}
    for elem in data:
        # получаем дату прогноза
        stamp = datetime.fromtimestamp(elem['dt'])
        date = stamp.strftime('%d.%m.%Y')
        # добавляем дату в словарь, если ее еще там нет
        if date not in forecasts:
            forecasts[date] = {}
        # получаем время прогноза
        time = stamp.strftime('%H:%M')
        # готовим погодные данные к сохранению
        main = elem['main']
        description = elem['weather'][0]['description']
        wind = elem['wind']
        # добавляем погодные данные по дате и времени
        forecasts[date][time] = (
            f"Температура {main['temp']} °C, {description}",
            f"Ощущается как {main['feels_like']} °C",
            f"Влажность {main['humidity']} %",
            f"Ветер {wind['speed']} м/c")
    return forecasts
# -----------------------------------------------------------------------------------------------------------

# Телеграм бот + прогноз погоды на несколько дней


