N = int(input('Введите количество учеников:')) # вводим кол-во учеников
data = []#создаем список для данных о каждом ученике
for i in range(N): #запускаем ввод данных об учениках
    line = input('Введите ИМЯ БАЛЛ1 БАЛЛ2 БАЛЛ3:').split()#вводим имя вместе с баллами
    data.append(line) #добавляем введенные данные в список
subject_1 = 0 #сумма баллов по предмету 1
subject_2 = 0 #сумма баллов по предмету 2
subject_3 = 0 #сумма баллов по предмету 3
for line in data: #о
бходим список 
    summa = int(line[1]) + int(line[2]) + int(line[3]) #находим сумму баллов 
    print(f'Сумма баллов ученика {line[0]}: {summa}') #выводим на экран сумму баллов
         #считаем сумму баллов для каждого предмета
    subject_1 += int(line[1])
    subject_2 += int(line[2]) 
    subject_3 += int(line[3]) 
#выводим на экран средний балл по каждому предмету
print(f'Средний балл по Предмету1: {subject_1/N}')
print(f'Средний балл по Предмету2: {subject_2/N}')
print(f'Средний балл по Предмету3: {subject_3/N}')