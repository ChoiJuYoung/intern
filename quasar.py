from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup
import json

def init():
    global entire_list
    f = open("quasar.txt", 'r')
    entire_list = json.loads(f.read())

def implement():
    url = "https://quasarzone.co.kr/bbs/board.php?bo_table=qb_saleinfo"
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")

    span_items = bs.find_all('span')
    for span in span_items:
        span.extract()

    item = bs.find_all('li', attrs={'class': 'list-item'})
    link = [it.a.attrs['href'] for it in item]
    title = [it.a.text.strip() for it in item]

    for li, ti in zip(link[4:], title[4:]):
        if li in entire_list.keys():
            if ti == entire_list[li]:
                continue
            print(li + "\n제목 수정: " + entire_list[li] + " => " + ti)
            entire_list[li] = ti
            save()
            continue
        entire_list[li] = ti
        save()
        print(li + "\n신규 정보: " + ti)


def save():
    f = open('quasar.txt', 'w')
    f.write(str(entire_list).replace("\'", "\""))

init()
implement()