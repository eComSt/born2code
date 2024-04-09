import json

human = {
    'name': 'Dima',
    'age': 18,
    'city': 'Moscow'
}

human_json = json.dumps(human)
# print(human_json)


human = {
    'имя': 'Дима',
    'возраст': 18,
    'город': 'Москва'
}

human_json = json.dumps(human, ensure_ascii=False, indent=4)
print(human_json)