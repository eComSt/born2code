from datetime import datetime
# from playsound import playsound
import time

def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return 'неверный формат, попробуйте снова!'
    else:
        if int(alarm_time[0:2]) < 24 and int(alarm_time[3:5]) < 60 and int(alarm_time[7:8]) < 60:
            return 'введено верно!'

while True:
    alarm_time = input('введите время будильника в формате часы:минуты:секунды: ')
    validate = validate_time(alarm_time)
    if validate == 'введено верно!':
        print(f'будильник установлен на {alarm_time}')
        print('ждите')
        break
    else:
        print(validate)
        continue

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[7:8])
while True:
    now = datetime.now()
    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second
    if alarm_hour == current_hour and alarm_min == current_min and alarm_sec == current_sec:
        print('Подъём!')
        # plays12ound('C:\\Users\\User\\.vscode\\extensions\\bimbapy\\alarm.mp3')
        break
