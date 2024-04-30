from functools import wraps
import logging

logging.basicConfig(level=logging.DEBUG, filename="py_log.log",filemode="w",
                    format="%(asctime)s %(levelname)s %(message)s")

def log_function_info(func):
    '''Декоратор, который выводит информацию о функции в консоль.'''
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'Вызвана функция {func.__name__}')
        logging.error(f'Документация: {func.__doc__}')
        return func(*args, **kwargs)
    return wrapper

@log_function_info
def add_book(title, author):
    '''Добавляет книгу с указанным названием и автором в каталог.'''
    if title not in books:
        books[title] = author
        print(f'Книга {title} автора {author} успешно добавлена.')

@log_function_info
def find_book(title):
    '''Ищет книгу по названию и возвращает статус наличия в каталоге'''
    if title in books:
        print(f'Поиск книги {title} в каталоге... Найдена!')
    else:
        print(f'Поиск книги {title} в каталоге... К сожалению, книга не найдена.')

books = {}
add_book('Властелин колец', 'Дж. Р. Р. Толкиен')
find_book('Властелин колец')
find_book('Гарри Поттер')
