import configparser
import telebot
config = configparser.ConfigParser()
config.read('config.ini')
token = config['DEFAULT']['token']
bot = telebot.TeleBot("7018542469:AAF8eACXN9IoJO56ae7Rd9HjRiVSRw5mMQ8")

@bot.message_handler(commands=['start'])
def start(message):
    kbrd = telebot.types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    button1 = telebot.types.KeyboardButton('Привет')
    button2 = telebot.types.KeyboardButton('Как дела?')
    kbrd.add(button1, button2)
    bot.send_message(message.chat.id, "Добрый день! Я небольшой эхо бот", reply_markup=kbrd)

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, "Я пока умею только повторять за вами!")

@bot.message_handler(commands=['goodbye'])
def start(message):
    bot.send_message(message.chat.id, "До свидания, было приятно пообщаться!")

@bot.message_handler(content_types=['text'])
def echo_message(message):
    if message.text == 'Привет':
        text = "Привет, " + message.from_user.first_name + "!"
    elif message.text == 'Как дела?':
        text = "Не плохо, а у вас?"
    else:
        text = message.text
    bot.reply_to(message, text)

bot.polling()