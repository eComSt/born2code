import requests
from datetime import datetime
API_KEY = "a8f6fef7a296bbce70aa16aca85698e3"

def get_coords(city_name):
    url = 'http://api.openweathermap.org/geo/1.0/direct?'
    params = {
        "q": city_name,
        "appid": API_KEY,
        "limit": 1
    }
    responce = requests.get(url, params=params)
    data = responce.json()[0]
    return data['lat'], data['lon']

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

print(get_weather('Saint-Petersburg'))
