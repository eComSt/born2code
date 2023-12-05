n = int(input()) #считаем с клавиатуры число n 
result = set() #сформируем пустое множество
for i in range(1, n + 1): #цикл для прохода по числам от 1 до n 
    result.add(i) #добавляем числа в множество
while True: #запускаем бесконечный цикл 
    ask = input() #считаем с клавиатуры ответ Вани
    if ask == 'HELP': #проверка, нужна ли помощь Ване
        print(result) #если просит, выводим на экран результат
        break #выходим из цикла
    else: #если Ваня не просит о помощи, значит он ввел числа
        ask_set = set() #создадим новое пустое множество
        for elem in ask.split():#убираем пробелы, перебираем элементы
            ask_set.add(int(elem)) #преобразуем элемент в целое число
    answer = input() #получаем ответ от Пети
    if answer == 'YES': #если «Да»
        result.intersection_update(ask_set) #ищем пересечение
    elif answer == 'NO': #если «Нет»
        result.difference_update(ask_set) #ищем вычитание
    if len(result)<2: #ОТГАДАЛ
        print(result)
        break