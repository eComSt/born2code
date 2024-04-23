import requests

# ВАШ КЛЮЧ для доступа к API сервиса Яндекс.Погода
API_KEY = 'ddb44d30-942f-4c09-a1ea-c912ea3e13cd'
# широта и долгота интересующего города
coords = (59.939099, 30.315877)
# строка с запросом к API Яндекс.Погоды
url = f'https://api.weather.yandex.ru/v2/forecast?'
# заголовок с ключом для доступа к API
headers = {'X-Yandex-API-Key': API_KEY}
# параметры запроса - широта, долгота и язык ответа
params = {'lat': coords[0],
          'lon': coords[1],
          'lang': 'ru_RU'}
# получаем ответ от сервиса при помощи GET-запроса
response = requests.get(url, headers=headers)
# конвертируем ответ из JSON в словарь
data = response.json()
# обращаемся к объекту fact для получения информации о погоде на данный момент
fact = data['fact']

# словарь со значениями поля is_thunder
is_thunder = {
    False: 'Грозы нет',
    True: 'Гроза есть'
}

# словарь со значениями поля prec_type
prec_type = {
    0: 'без осадков',
    1: 'дождь',
    2: 'дождь со снегом',
    3: 'снег',
    4: 'град'
}

# словарь со значениями поля prec_strength
prec_strength = {
    0: 'без осадков',
    0.25: 'слабый дождь/слабый снег',
    0.5: 'дождь/снег',
    0.75: 'сильный дождь/сильный снег',
    1: 'сильный ливень/очень сильный снег'
}

# выводим на экран информацию о температуре
print(f"Температура: {fact['temp']} °C")
# выводим на экран информацию о том, есть ли сейчас гроза 
print(is_thunder[fact['is_thunder']])
# выводим на экран информацию о типе осадков
print(f"Тип осадков:{prec_type[fact['prec_type']]}")
# выводим на экран информацию о силе осадков
print(f"Сила осадков:{prec_strength[fact['prec_strength']]}")