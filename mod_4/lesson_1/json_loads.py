import json
str = '{"имя": "Дима", "возраст": 18, "город": "Москва"}'
data = json.loads(str)
print(type(data))