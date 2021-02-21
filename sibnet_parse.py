from bs4 import BeautifulSoup
import requests
import urllib

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
}



def getHTML(url): #получает ссылку на плеер сибнета
    req = requests.get("https://video.sibnet.ru/shell.php?videoid=" + url, headers=headers)
    return(req.text)

def getSrc(html):#получает ссылку на файл аниме
    try:
        soup = BeautifulSoup(html, "lxml")
        raw_src = soup.find(class_="videojs_player").next_sibling#получает тонну мусора с нужной ссылкой
        
        with open('tmp.txt','w') as f:#пишет полученый мусор в файл ставя пропус строки вместо кавычек
            f.write(str(raw_src).replace('"' , '\n'))

        word = u'/v/'
        with open('tmp.txt', encoding='utf-8') as file: #ищет строку начинающуюся с /v/
            for line in file:
                if word in line:
                    path =line
            
        path = "https://video.sibnet.ru" + path.strip()
        r = requests.head(path, headers={ "referer": "https://video.sibnet.ru"}) #заходит на ссылку с хедером сайта
        src=(r.headers["Location"])#получает ссылку на сам файл 
        src = "https:" + src

        return(src)
    except:
        return "error getSrc maybe it not standart type of page"