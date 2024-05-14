import telebot
import configparser
import random
config = configparser.ConfigParser()
config.read('config.ini')
token = "7018542469:AAF8eACXN9IoJO56ae7Rd9HjRiVSRw5mMQ8"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    kbrd = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('Привет')
    button2 = telebot.types.KeyboardButton('Как дела?')
    button3 = telebot.types.KeyboardButton('Расскажи интересный факт')
    kbrd.add(button1, button2, button3)
    bot.send_message(message.chat.id, "Добрый день! Я небольшой эхо бот", reply_markup=kbrd)



@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, "Я пока умею только повторять за вами!")

@bot.message_handler(commands=['goodbye'])
def start(message):
    bot.send_message(message.chat.id, "До свидания, было приятно пообщаться!")

@bot.message_handler(content_types=['text'])
def echo_message(message):
    facts = [
    "Хамелеоны могут двигать глазами в разных направлениях одновременно.",
    "Электрический угорь может вырабатывать энергию, способную зажечь 12 лампочек.",
    "Морские котики могут задерживать дыхание на два часа."
    ]
    print(message.text)
    if message.text == 'Привет':
        text = "Привет, " + message.from_user.first_name + "!"
    elif message.text == 'Как дела?':
        text = "Не плохо, а у вас?"
    elif message.text == 'Расскажи итересный факт':
        text = random.choice(facts)
    else:
        text = message.text
    bot.reply_to(message, text)



bot.polling()