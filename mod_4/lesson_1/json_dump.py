import json
 
human = {
    'name': 'Dima',
    'age': 18,
    'city': 'Moscow'
}
 
with open('human.json', 'w') as file:
    json.dump(human, file)


human = {
    'имя': 'Дима',
    'возраст': 18,
    'город': 'Москва'
}
with open('human2.json', 'w', encoding='utf-8') as file:
    json.dump(human, file, ensure_ascii=False, indent=4,skipkeys=True)