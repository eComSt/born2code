import telebot
from api import get_weather
token = "7018542469:AAF8eACXN9IoJO56ae7Rd9HjRiVSRw5mMQ8"
bot = telebot.TeleBot(token)
USERS = {}
@bot.message_handler(commands=['start'])
def start(message):
    hello = "Привет, я бот, который показывает погоду в городе"
    bot.send_message(message.chat.id, hello)

def change_city(message):
    bot.send_message(message.chat.id, "Введите название города")
    bot.register_next_step_handler(message, save_city)

def save_city(message):
    USERS[str(message.chat.id)] = message.text
    bot.send_message(message.chat.id, "Город сохранен", reply_markup = menu())

def menu():
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width = 3, resize_keyboard=True, one_time_keyboard=False)
    but1 = telebot.types.KeyboardButton("Погода в городе")
    but2 = telebot.types.KeyboardButton('Подробный прогноз на дату')
    but3 = telebot.types.KeyboardButton('Сменить город')
    keyboard.add(but1, but2, but3)
    return keyboard

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == "Погода в городе":
        bot.send_message(message.chat.id, get_weather(USERS[str(message.chat.id)]))
    elif message.text == "Подробный прогноз на дату":
        bot.send_message(message.chat.id, 'Данная функция находится в разработке')
    elif message.text == "Сменить город":
        change_city(message)
    else:
        bot.send_message(message.chat.id, "Неизвестная команда")

bot.polling()
