dictionary = {
    'apple': 'яблоко',
    'cat': 'кот',
    'door': 'дверь',
    'sunny': 'солнечный',
    'Pudge': 'Пудж',
    'winter': 'зима',
    'cute': 'милый',
    'language': 'язык',
    'dog': 'собака',
    'milk': 'молоко',
    'orange':  'оранжевый',
    1: 'один',
    1.5: 'один c половиной',
    '1': None,
}
dictionary2 = {
    'orange': 'апельсин',
    'banana': 'банан',
    'car': 'машина',
    'sweets': 'конфеты',
}
songs = {
    'Bad Guy': 3,
    'Thunder': 3,
    'Sweater Weather': 4,
    'Numb': 3,
    'Karma Police': 4,
    'Enjoy the Silence': 4,
    'Obstacles': 3,
    'Crosses': 2,
    'Unnamed Feeling': 7
}
dictionary.update(dictionary2)
dictionary.update(songs)
del dictionary[1]
x = dictionary.pop(1.5)
y = dictionary.popitem()
# word = input("Введите слово: ")
# if word not in dictionary:
#     translate = input("Введите перевод: ")
#     dictionary[word] = translate
# print(f"Перевод слова {word}: {dictionary[word]}")
# for i,j in dictionary.items():
#     print(i,j)
# dictionary.clear() 
# print(len(dictionary))
# print(dictionary.values())
dict3 = dictionary.copy()
dictionary["apple"] = "42"
# print(dict3["apple"])
# print(dictionary["apple"])

print(dictionary.setdefault('aple','Нет такого слова в словаре'))
