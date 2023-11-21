catalog_books = {

}
# Цикл для работы
while True:
    print('Список возвожных действий: ')
    print('1 - Доб книгу')
    print('2 - Поиск по названию')
    print('3 - Удаление книги книгу')
    print('4 - Показать информацию о всех книгах в каталоге')
    print('0')
    # Запрашиевм у пользователя номер действия
    user_choise = int(input('№ Действия: '))

    if user_choise == 0:
        print('До свидания')
        break
    elif user_choise == 1:
        titile = input('Введите названия книги: ')
        while titile in catalog_books:
            titile = input('Повторите Введите названия книги: ')
        autor = input('Имя автора')
        catalog_books[titile] = autor

    # Проверка 2
    elif user_choise == 2:
        titile = input('Введите названия книги: ')
        if titile in catalog_books:
            print(f'Название, {titile}, Автор: {catalog_books[titile]}')
        else:
            print('Книга не найдена')
    #Проверка выбор 3

    elif user_choise == 3:
        titile = input('Введите названия книги: ')
        if titile in catalog_books:
            del catalog_books[titile]
            print('Книга удалена')
        else:
            print('Книги нету')
    # Проверка 4
    elif user_choise == 4:
        # books - ключ
        for books in catalog_books:
            print(f'Название: {books}, Автор: {catalog_books[books]}')
    # 5
    else:
        print('Неверное действие')