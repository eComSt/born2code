import json
 
with open('human.json' , encoding='utf-8') as file:
    human_data = json.load(file)
print(type(human_data))