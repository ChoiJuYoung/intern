import weather as w
from datetime import datetime
from bs4 import BeautifulSoup

def chk_time(func):
    def _chk_time():
        start = datetime.now()
        func()
        end = datetime.now()
        print(str(end - start))
    return _chk_time()

bsObject = w.init("회기동")
#print(bsObject)

@chk_time
def normal():
    for _ in range(100000):
        print()
        
@chk_time
def bs():
    for _ in range(100000):
        print()