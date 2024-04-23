import time 
import requests

def benchmark(func):
    def wrapper():
        start = time.time()
        out = func()
        end = time.time()
        print('Время выполнения: {} секунд.'.format(end-start))
        return out
    return wrapper

@benchmark
def fetch_webpage():
    webpage = requests.get('https://google.com')
    return webpage

fetch_webpage()