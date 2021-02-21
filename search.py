
from bs4 import BeautifulSoup
import requests
import urllib.parse

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
}

def generatorURL(search_name): #get search link for website
    url = "https://animenime.ru/?s=" + urllib.parse.quote_plus(search_name)
    return(url)

def getHTML(url): #get html from website
    req = requests.get(url, headers=headers)
    return(req.text)

def getInfo(html):
    soup = BeautifulSoup(html, "lxml")
    Info = soup.find_all(class_="title_gr")
    return(Info)

def getTitle(Info): #get names anime on page
    TitleList = list()
    for anime_raw_title in Info:
        anime_title = anime_raw_title.find("h2")
        title = str(anime_title).replace("<h2>", "").replace("</h2>", "")
        TitleList.append(title)
    return(TitleList)

def getHref(Info): #get links anime on page
    HrefList = list()
    for anime_href in Info:
        href = anime_href.find("a").get("href")
        HrefList.append(href)
    return(HrefList)
    

def anime_count(HrefList): #количество найденых аниме
    return(len(HrefList))





#if __name__ == __main__:
#print(URL)
#   i = 0
#    while(i !=len(TitleList)):
#       print(TitleList[i])
#        print(HrefList[i])
#        i = i + 1


