dictionary = {}
try: dictionaryfile = open('dictionary.txt', 'x')
except FileExistsError:
    with open('dictionary.txt') as dictionaryfile:
        while True:
            line = dictionaryfile.readline()[:-1]
            if not line:
                break
            word, translate = (i for i in line.split(' - '))
            dictionary[word] = translate
            # print(dictionary)

dictionaryfile = open('dictionary.txt', 'a')

word = input('Введите слово: ').lower()
if word not in dictionary:
    translate = input('Введите перевод: ').lower()
    dictionaryfile.write(f"{word} - {translate}\n")
    dictionary[word] = translate
print(f"Перевод слова {word.capitalize()}: {dictionary[word].capitalize()}")

dictionaryfile.close()