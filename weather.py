from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup

def init(where):
    url = "https://search.naver.com/search.naver?query=" + parse.quote(where + "+날씨")
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")

    return bsObject

def getWeather(bsObject, where):
    loc = bsObject.split("<em>")[7].split("<")[0]
    weather = bsObject.split("<p class=\"cast_txt\">")[1].split("아")[0]
    temp = bsObject.split("<span class=\"todaytemp\">")[1].split("<")[0]
    ltemp = bsObject.split("<span class=\"num\">")[1].split("<")[0]
    htemp = bsObject.split("<span class=\"num\">")[2].split("<")[0]
    ftemp = bsObject.split("<span class=\"num\">")[3].split("<")[0]
    mrain = bsObject.split("<span class=\"num\">")[8].split("<")[0]
    arain = bsObject.split("<span class=\"num\">")[9].split("<")[0]
    dust = bsObject.split("<span class=\"num\">")[5].split("<")[0]
    fdust = bsObject.split("<span class=\"num\">")[6].split("<")[0]
    ozone = bsObject.split("<span class=\"num\">")[7].split("<")[0]
    wind = bsObject.split("<span>")[47].split("<")[0]
    humid = bsObject.split("<span>")[63].split("<")[0]
    tmt = bsObject.split("<span class=\"todaytemp\">")[2].split("<")[0]
    tat = bsObject.split("<span class=\"todaytemp\">")[3].split("<")[0]
    tmw = bsObject.split("<p class=\"cast_txt\">")[2].split("<")[0]
    taw = bsObject.split("<p class=\"cast_txt\">")[3].split("<")[0]
    tmr = bsObject.split("<span class=\"num\">")[10].split("<")[0]
    tar = bsObject.split("<span class=\"num\">")[11].split("<")[0]
    datmt = bsObject.split("<span class=\"todaytemp\">")[4].split("<")[0]
    datat = bsObject.split("<span class=\"todaytemp\">")[5].split("<")[0]
    datmw = bsObject.split("<p class=\"cast_txt\">")[4].split("<")[0]
    dataw = bsObject.split("<p class=\"cast_txt\">")[5].split("<")[0]
    datmr = bsObject.split("<span class=\"num\">")[12].split("<")[0]
    datar = bsObject.split("<span class=\"num\">")[13].split("<")[0]
    t = bsObject.split("<span class=\"day_info\">")[2].split(" ")[0]
    dt = bsObject.split("<span class=\"day_info\">")[3].split(" ")[0]
    loc = loc.strip()
    text1 = (where + "의 기상 정보\n" + "(" + "위치: " + loc + ")" + "\n\n날씨: " + weather  + "음\n" + "최저/최고 기온: " + ltemp + "º / " + htemp + "º\n" + "현재 기온: " + temp + "º\n" + "체감온도: " + ftemp + "º\n" + "습도: " + humid + "%\n" + "풍속: " + wind + "m/s" + "\n오전 강수확률: " + mrain + "%" + "\n오후 강수확률: " + arain + "%" + "\n미세먼지: " + dust + "\n초미세먼지: " + fdust + "\n오존: " + ozone)
    text2 = ("내일(" + t + ") 날씨\n\n" + "오전: " + tmw + ", " + tmt + "º\n" + "강수확률: " + tmr + "%\n" + "오후: " + taw + ", " + tat + "º\n" + "강수확률: " + tar + "%\n\n\n" + "모레(" + dt + ") 날씨\n\n" + "오전: " + datmw + ", " + datmt + "º\n" + "강수확률: " + datmr + "%\n" + "오후: " + dataw + ", " + datat + "º\n" + "강수확률: " + datar + "%")
    
    return [text1, text2]

def getWeather_bs(bs, where):
    loc = bs.find('span', attrs={'class': 'btn_select'}).text
    weather = bs.find('p', attrs={'class': 'cast_txt'}).text
    temp_all = [li.text for li in bs.find_all('span', attrs={'class': 'todaytemp'})]
    temp = temp_all[0]
    #lhtemp = [[t.text for t in b.find('dl').find_all('span')] for b in bs.find_all('li', attrs={'class': 'date_info today'})]
    ltemp = bs.find('span', attrs={'class': 'min'}).text
    htemp = bs.find('span', attrs={'class': 'max'}).text
    ftemp = bs.find('span', attrs={'class': 'sensible'}).find('em').text
    rain = [li.find('span', attrs={'class': 'num'}).text for li in bs.find_all('li', attrs={'class': 'date_info today'})]
    mrain = rain[0]
    arain = rain[1]
    d = [d.text for d in bs.find('dl', attrs={'class': 'indicator'}).find_all('span', attrs={'class': 'num'})]
    dust = d[0]
    fdust = d[1]
    ozone = d[2]
    wind = bs.find('div', attrs={'class': 'info_list wind _tabContent'}).find('span').text
    humid = bs.find('div', attrs={'class': 'info_list humidity _tabContent'}).find('span').text
    tmt = temp_all[1]
    tat = temp_all[2]
    
    

def getQuasa():
    url = "https://quasarzone.co.kr/bbs/board.php?bo_table=qb_saleinfo"
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    bsObject = str(bsObject)

    return bsObject