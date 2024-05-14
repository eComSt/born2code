
import requests
q = "https://yandex.ru/pogoda/novosibirsk?lat=55.030199&lon=82.92043"
data = requests.get(q)
print(data.text)