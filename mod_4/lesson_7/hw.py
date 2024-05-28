import requests
from datetime import timedelta
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

def get_sun_time(city_name):
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
    sunrise = data['sys']['sunrise']
    sunset = data['sys']['sunset']
    return timedelta(seconds = sunset - sunrise)

city = input("Введите название города: ")
print(get_sun_time(city))