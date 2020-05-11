import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import json
import sys

def init():
    global entire_list
    entire_list = {}
    #f = open("C:\\quasar.txt", 'r')
    #entire_list = json.loads(f.read())

def implement():
    res = []
    url = "https://quasarzone.co.kr/bbs/qb_saleinfo"
    html = urlopen(url)
    bs = BeautifulSoup(html, "html.parser")

    item = bs.find_all('a', attrs={'class': 'subject-link'})
    link = ["https://quasarznoe.co.kr" + it.attrs['href'] for it in item]
    title = [it.text.strip() for it in item]

    for li, ti in zip(link[4:], title[4:]):
        if li in entire_list.keys():
            if ti == entire_list[li]:
                continue
            res.append("제목 수정: " + entire_list[li] + " => " + ti + "\n" + li)
            entire_list[li] = ti
            continue
        entire_list[li] = ti
        res.append("신규 정보: " + ti + "\n" + li)
    return res

init()
print(implement())