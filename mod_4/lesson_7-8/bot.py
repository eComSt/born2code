import telebot
from api import get_weather,get_daily_forecasts
token = "7018542469:AAF8eACXN9IoJO56ae7Rd9HjRiVSRw5mMQ8"
bot = telebot.TeleBot(token)
USERS = {}
FORECASTS = {}

def days_buttons(message):
   FORECASTS.update(get_daily_forecasts(USERS[str(message.chat.id)]))
   days = telebot.types.InlineKeyboardMarkup()
   for date in FORECASTS.keys():
     button = telebot.types.InlineKeyboardButton(text=date, callback_data=date)
     days.add(button)
   bot.send_message(message.chat.id, text='Выберите нужный день',   	reply_markup=days)


@bot.message_handler(commands=['start'])
def start(message):
    hello = "Привет, я бот, который показывает погоду в городе"
    bot.send_message(message.chat.id, hello)
    change_city(message)

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

def get_cur_weather(message):
    try:
        weather = get_weather(USERS[str(message.chat.id)])
        answear = "\n".join(weather)
    except:
        answer = 'Погода по данному городу не найдена'
    bot.send_message(message.chat.id, answear)

@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == "Погода в городе":
        get_cur_weather(message)
    elif message.text == "Подробный прогноз на дату":
        days_buttons(message)
    elif message.text == "Сменить город":
        change_city(message)
    else:
        bot.send_message(message.chat.id, "Неизвестная команда")

bot.infinity_polling()
