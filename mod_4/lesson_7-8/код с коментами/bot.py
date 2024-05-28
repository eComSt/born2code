# Телеграм-бот + прогноз погоды на несколько дней

import telebot
# подключаем функции для получения погодных данных
from api import get_weather, get_daily_forecasts

token = ''
bot = telebot.TeleBot(token)

USERS = {}
# словарь для хранения прогнозов погоды
FORECASTS = {}

# обработка вызова команды /start
@bot.message_handler(commands=['start'])
def start(message):
    hello = 'Добрый день! Я бот, показывающий прогноз погоды.'
    bot.send_message(message.chat.id, text=hello)
    change_city(message)

# обработка ситуации, когда пользователь хочет указать новое название города
def change_city(message):
    bot.send_message(message.chat.id, text='Укажите название города')
    bot.register_next_step_handler(message, save_city)

# сохранение введенного пользователем города
def save_city(message):
    USERS[str(message.chat.id)] = message.text
    bot.send_message(message.chat.id, text=f'Город {message.text} успешно сохранен!', reply_markup=menu())

# создание клавиатуры с тремя кнопками
def menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=False)
    button1 = telebot.types.KeyboardButton('Текущая погода')
    button2 = telebot.types.KeyboardButton('Подробный прогноз на дату')
    button3 = telebot.types.KeyboardButton('Сменить город')
    keyboard.add(button1, button2, button3)
    return keyboard

# получение текущей погоды для указанного города
def current_weather(message):
    try:
        weather = get_weather(USERS[str(message.chat.id)])
        answer = '\n'.join(weather)
    except:
        answer = 'Погода по данному городу не найдена'
    bot.send_message(message.chat.id, text=answer)

# создание inline-клавиатуры с датами прогнозов погоды
def days_buttons(message):
    # сохранение в словарь прогнозов погоды для указанного города
    FORECASTS.update(get_daily_forecasts(USERS[str(message.chat.id)]))
    # InlineKeyboardMarkup() - класс для создания inline-клавиатуры (клавиатура, встроенная в сообщение)
    days = telebot.types.InlineKeyboardMarkup()
    # наполнение клавиатуры кнопками с датами
    for date in FORECASTS.keys():
        '''InlineKeyboardButton() - класс для создания inline-кнопки
        text - текст кнопки, callback_data - данные, отправляемые боту после нажатия на кнопку'''
        button = telebot.types.InlineKeyboardButton(text=date, callback_data=date)
        days.add(button)
    # отображение сообщения с клавиатурой в чате
    bot.send_message(message.chat.id, text='Выберите нужный день', reply_markup=days)

'''callback_query_handler() - декоратор, позволяющий обрабатывать callback-запросы, приходящие от inline-кнопок
callback-запросы генерируются, когда пользователь нажимает на inline-кнопку
Данный декоратор принимает на вход функцию фильтрации, которая определяет, какие именно callback-запросы
должна обрабатывать декорируемая функция.'''
# функция фильтрации проверяет, что нажата кнопка с датой (там нет символа ':')
@bot.callback_query_handler(func=lambda call: ':' not in call.data)
# создание inline-клавиатуры с почасовыми метками прогнозов погоды
def hours_buttons(call):
    # получение данных из нажатой кнопки (дата прогноза)
    date = call.data
    # создание и наполнение inline-клавиатуры кнопками с часами
    hours = telebot.types.InlineKeyboardMarkup()
    for hour in FORECASTS[date].keys():
        button = telebot.types.InlineKeyboardButton(text=hour, callback_data=f'{date} {hour}')
        hours.add(button)
    # отображение сообщения с клавиатурой в чате
    bot.send_message(call.message.chat.id, text='Выберите нужное время', reply_markup=hours)

# функция фильтрации проверяет, что нажата кнопка с временем (там есть символ ':')
@bot.callback_query_handler(func=lambda call: ':' in call.data)
# отображение прогноза погоды для указанной даты и времени
def show_forecast(call):
    # получаем время и дату
    data = call.data.split()
    date, hour = data[0], data[1]
    # получаем погодные данные из словаря по указанным дате и времени
    forecast = FORECASTS[date][hour]
    # формируем строку с данными о прогнозе
    answer = f'Прогноз на {date}, {hour}\n' + '\n'.join(forecast)
    # отправляем прогноз в чат
    bot.send_message(call.message.chat.id, text=answer)
    
@bot.message_handler(content_types=['text'])
def check_text(message):
    if message.text == 'Текущая погода':
        current_weather(message)
    elif message.text == 'Сменить город':
        change_city(message)
    elif message.text == 'Подробный прогноз на дату':
        days_buttons(message)
    else:
        bot.reply_to(message, 'К сожалению, я вас не понимаю')

bot.polling()
