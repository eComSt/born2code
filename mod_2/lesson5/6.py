words = ['красный', 'синий', 'оранжевый', 'белый']
long_words = list(filter(lambda line: len(line) > 5, words))
print(long_words)

words = ['шалаш', 'кот', 'топот', 'бег']
#указываем последовательность, из которой будем брать данные	
pal_words = list(filter(lambda word: word == word[::-1], words))
print(pal_words)