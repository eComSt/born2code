# import requests
# response = requests.get('https://yandex.ru/pogoda/')
# print(response.text)
import requests

# координаты населенного пункта в формате "широта, долгота"
coords = (55.0415, 82.9346)
# ваш ключ с доступом к API Яндекс.Погоды
API_KEY = 'ddb44d30-942f-4c09-a1ea-c912ea3e13cd'
# начальная часть GET-запроса к API Яндекс.Погоды
url = 'https://api.weather.yandex.ru/v2/forecast?'
# заголовок запроса с ключом доступа к API
headers = {'X-Yandex-API-Key': API_KEY}
# параметры запроса - широта, долгота и язык ответа
params = {'lat': coords[0],
          'lon': coords[1],
          'lang': 'ru_RU'}
# отправляем GET-запрос с указанными заголовками и параметрами
data = requests.get(url, headers=headers, params=params).json()
# отдельно сохраняем информацию о погоде на текущий момент времени
fact = data['fact']
# текущая температура
print(f"Температура {fact['temp']}°C")
# как ощущается температура
print(f"Ощущается как {fact['feels_like']}°C")
# скорость ветра
print(f"Скорость ветра {fact['wind_speed']} м/c")
# словарь с возможными значениями направления ветра и их расшифровками
winds = {
    'nw': 'северо-западное',
    'n': 'северное',
    'ne': 'северо-восточное',
    'e': 'восточное',
    'se': 'юго-восточное',
    's': 'южное',
    'sw': 'юго-западное',
    'w': 'западное',
    'c': 'штиль'
}
# направление ветра
print(f"Направление ветра {winds[fact['wind_dir']]}")
# давление в миллиметрах ртутного столба
print(f"Атмосферное давление {fact['pressure_mm']} мм.")
# pprint(response.json())