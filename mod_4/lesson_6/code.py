import requests # подключаем библиотеку для отправки GET-запросов
# координаты населенного пункта в формате "широта, долгота"
coords = (59.9386, 30.3141)
API_KEY = 'dc610ddd2e0bfa14d7ae1e16c57b389e' # ВАШ ключ с доступом к OpenWeather API
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