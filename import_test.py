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

html = '<td id="td1" class="title">' \
       '  <div class="tit3">' \
       '    <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a>' \
       '  </div>' \
       '  <div class="tit4">' \
       '    hi' \
       '  </div>' \
       '</td>'

@chk_time
def normal():
    for _ in range(100000):
        html.split("<td id=\"td1\" class=\"title\">")
        html.split("<td id=\"td1\" class=\"title\">")
        html.split("<td id=\"td1\" class=\"title\">")
        
@chk_time
def bs():
    for _ in range(100000):
        html.find('td')
        html.find('td')
        html.find('td')