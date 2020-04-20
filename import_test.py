from weather import getWeather
from weather import getWeather2
from weather import getQuasa
from datetime import datetime

def chk_time(func):
    def _chk_time():
        start = datetime.now()
        func()
        end = datetime.now()
        print(str(end - start))
    return _chk_time()

@chk_time
def normal():
    getWeather("회기동")

@chk_time
def normal2():
    getWeather2("회기동")