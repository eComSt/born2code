import json

# Читаем данные из файла
with open('countries_languages.json', 'r',encoding="utf-8") as f:
    countries_languages = json.load(f)

# Создаем новый словарь
# languages_countries = {item['language']:[item['country']] if item['language'] not in languages_countries else languages_countries[item['language']]+item['language'] for item in countries_languages}
languages_countries =  {}
# Перебираем исходный словарь
for item in countries_languages:
    # Если языка еще нет в новом словаре, добавляем его и присваиваем ему список с текущей страной
    if item['language'] not in languages_countries:
        languages_countries[item['language']] = [item['country']]
    # Если язык уже есть в новом словаре, добавляем к его списку текущую страну
    else:
        languages_countries[item['language']].append(item['country'])

# Выводим получившийся словарь
for language, countries in languages_countries.items():
    print(f'{language}: {countries}')
