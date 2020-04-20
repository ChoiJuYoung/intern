from bs4 import BeautifulSoup

html = '<td id="td1" class="title">' \
       '  <div class="tit3">' \
       '    <a href="/movie/bi/mi/basic.nhn?code=161242" title="범죄도시">범죄도시</a>' \
       '  </div>' \
       '  <div class="tit4">' \
       '    hi' \
       '  </div>' \
       '</td>'

def ex1():
    bs = BeautifulSoup(html, 'html.parser')
    print(bs, type(bs))

    tag = bs.a
    print(tag, type(tag))

def ex2():
    bs = BeautifulSoup(html, 'html.parser')

    tag = bs.td
    print(tag['class'])
    


ex1()
ex2()