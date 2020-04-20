import weather as w
from datetime import datetime

def chk_time(func):
    def _chk_time():
        start = datetime.now()
        func()
        end = datetime.now()
        print(str(end - start))
    return _chk_time()

bsObject = w.init("회기동")
print(bsObject)


@chk_time
def normal():
    for _ in range(1000):
        w.getWeather(bsObject, "회기동")

@chk_time
def normal2():
    for _ in range(1000):
        w.getWeather2(bsObject, "회기동")