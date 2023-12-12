import datetime, time, os

os.system('clear')
NY = datetime.datetime(2024, 1, 1)
while True:
    now = datetime.datetime.now()
    NY = datetime.datetime(2024, 1, 1)
    d = NY-now          
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    print('\rДо нового года: {} дней {} часа {} мин {} сек.'.format(d.days, hh, mm, ss),end = "")
    time.sleep(0.5)
