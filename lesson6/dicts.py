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
}

word = input("Введите слово: ")
if word not in dictionary:
    translate = input("Введите перевод: ")
    dictionary[word] = translate
print(f"Перевод слова {word}: {dictionary[word]}")

