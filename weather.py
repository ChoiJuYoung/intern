from urllib.request import urlopen
from urllib import parse
from bs4 import BeautifulSoup

def init(where):
    url = "https://search.naver.com/search.naver?query=" + parse.quote(where + "+날씨")
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    bsObject = str(bsObject)

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

def getWeather2(bsObject, where):

    res = {}
    
    res["loc"] = bsObject.split("<em>")[7].split("<")[0].strip()
    res["weather"] = bsObject.split("<p class=\"cast_txt\">")[1].split("아")[0]
    res["temp"] = bsObject.split("<span class=\"todaytemp\">")[1].split("<")[0]
    res["ltemp"] = bsObject.split("<span class=\"num\">")[1].split("<")[0]
    res["htemp"] = bsObject.split("<span class=\"num\">")[2].split("<")[0]
    res["ftemp"] = bsObject.split("<span class=\"num\">")[3].split("<")[0]
    res["mrain"] = bsObject.split("<span class=\"num\">")[8].split("<")[0]
    res["arain"] = bsObject.split("<span class=\"num\">")[9].split("<")[0]
    res["dust"] = bsObject.split("<span class=\"num\">")[5].split("<")[0]
    res["fdust"] = bsObject.split("<span class=\"num\">")[6].split("<")[0]
    res["ozone"] = bsObject.split("<span class=\"num\">")[7].split("<")[0]
    res["wind"] = bsObject.split("<span>")[47].split("<")[0]
    res["humid"] = bsObject.split("<span>")[63].split("<")[0]
    res["tmt"] = bsObject.split("<span class=\"todaytemp\">")[2].split("<")[0]
    res["tat"] = bsObject.split("<span class=\"todaytemp\">")[3].split("<")[0]
    res["tmw"] = bsObject.split("<p class=\"cast_txt\">")[2].split("<")[0]
    res["taw"] = bsObject.split("<p class=\"cast_txt\">")[3].split("<")[0]
    res["tmr"] = bsObject.split("<span class=\"num\">")[10].split("<")[0]
    res["tar"] = bsObject.split("<span class=\"num\">")[11].split("<")[0]
    res["datmt"] = bsObject.split("<span class=\"todaytemp\">")[4].split("<")[0]
    res["datat"] = bsObject.split("<span class=\"todaytemp\">")[5].split("<")[0]
    res["datmw"] = bsObject.split("<p class=\"cast_txt\">")[4].split("<")[0]
    res["dataw"] = bsObject.split("<p class=\"cast_txt\">")[5].split("<")[0]
    res["datmr"] = bsObject.split("<span class=\"num\">")[12].split("<")[0]
    res["datar"] = bsObject.split("<span class=\"num\">")[13].split("<")[0]
    res["t"] = bsObject.split("<span class=\"day_info\">")[2].split(" ")[0]
    res["dt"] = bsObject.split("<span class=\"day_info\">")[3].split(" ")[0]
    text1 = (where + "의 기상 정보\n" + "(" + "위치: " + res["loc"] + ")" + "\n\n날씨: " + res["weather"]  + "음\n" + "최저/최고 기온: " + res["ltemp"] + "º / " + res["htemp"] + "º\n" + "현재 기온: " + res["temp"] + "º\n" + "체감온도: " + res["ftemp"] + "º\n" + "습도: " + res["humid"] + "%\n" + "풍속: " + res["wind"] + "m/s" + "\n오전 강수확률: " + res["mrain"] + "%" + "\n오후 강수확률: " + res["arain"] + "%" + "\n미세먼지: " + res["dust"] + "\n초미세먼지: " + res["fdust"] + "\n오존: " + res["ozone"])
    text2 = ("내일(" + res["t"] + ") 날씨\n\n" + "오전: " + res["tmw"] + ", " + res["tmt"] + "º\n" + "강수확률: " + res["tmr"] + "%\n" + "오후: " + res["taw"] + ", " + res["tat"] + "º\n" + "강수확률: " + res["tar"] + "%\n\n\n" + "모레(" + res["dt"] + ") 날씨\n\n" + "오전: " + res["datmw"] + ", " + res["datmt"] + "º\n" + "강수확률: " + res["datmr"] + "%\n" + "오후: " + res["dataw"] + ", " + res["datat"] + "º\n" + "강수확률: " + res["datar"] + "%")
    
    return [text1, text2]

def getQuasa():
    url = "https://quasarzone.co.kr/bbs/board.php?bo_table=qb_saleinfo"
    html = urlopen(url)
    bsObject = BeautifulSoup(html, "html.parser")
    bsObject = str(bsObject)

    return bsObject