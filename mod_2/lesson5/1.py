#«Максимальная длина слова» В программе хранится список со строками различной длины. Необходимо найти и вывести на экран строку с максимальной длиной.
words = ['четыре', 'восемь', 'пятнадцать', 'восемнадцать']
max_word = ''#создаем пустую строку для хранения самого длинного слова
for word in words: #перебираем строки в списке
    if len(word) > len(max_word): #если длина текущей строки больше 
        max_word = word #обновляем значение переменной
print(max_word) #выводим итоговое значение на экран