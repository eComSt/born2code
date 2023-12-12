data = {  #создадим словарь с данными
    'Петя': {'Физика': 50, 'Математика': 80, 'Биология': 90}, 
    'Ваня': {'Математика': 65, 'Химия': 64, 'Физика': 90, 'РЯ': 78},
    'Катя': {'РЯ': 45, 'История': 57, 'Математика': 87},
}
for name, subjects in data.items(): #перебираем ключи и значения словаря
         #находим сумму элементов списка с баллами
    print(f'Сумма баллов ученика {name}:{sum(subjects.values())}') 
subject_scores = {} #создадим словарь для предметов и соответствующих баллов
for line in data.values(): #перебираем словари с предметами и баллами
    for subject in line.keys(): #перебираем предметы
        if subject in subject_scores: #проверяем наличие предмета в словаре
            subject_scores[subject].append(line[subject])#добавляем баллы в список
        else: #если предмета нет в словаре
            subject_scores[subject] = [line[subject]] #создаем новый объект словаря
for subject, scores in subject_scores.items(): #выводим средние баллы по предметам 
    print(f'Средний балл по предмету {subject}:{sum(scores)/ len(scores)}')