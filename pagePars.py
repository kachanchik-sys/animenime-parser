from bs4 import BeautifulSoup
import requests
import urllib

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0"
}


def getHTML(url): #get html from website
    req = requests.get(url, headers=headers)
    return(req.text)

def getPhoto(html): #получает ссылку на фото и скачивает его 
    try:
        soup = BeautifulSoup(html, "lxml")
        raw_src = soup.find("div", class_="tc-info-poster").find("img").get("src")
        src = "https://animenime.ru" + raw_src
    
        response = requests.get(src)
        if response.status_code == 200:
            with open('./Image.jpg','wb') as f:
                f.write(response.content)
            return(src)
        else:
            return (str("error"))
    except:
        return("exeption photo")

def getDescription(html):#получает описание со страницы обрезая его до 250 символов
    try:
        soup = BeautifulSoup(html, "lxml")
        description = soup.find("div", class_="tc-info-AN-h4-description").find("h4").text

        if len(description) > 250:
            description = description[0:250].rstrip()
            if description[-1] == "." or ",":
                i = len(description) - 1
                description = description[0:i]
            description = description + "..."
            return(description)
        else:
            return(description)
    except:
        return("exeption descruption")
    

def checkBlock(html):#проверяет заблокированно ли аниме
    try:
        soup = BeautifulSoup(html, "lxml")
        block_status = soup.find("div", class_="lock-content-txt").text.strip()
        return(True)
    except:
        return(False)

def getVideoVoiced(html):#получает id аниме с озвучкой
    try:
        soup = BeautifulSoup(html, "lxml")
        num = soup.find_all(class_ ="sStl")
        videoplayers= soup.find_all(class_ = "svb")
        n = len (num) / len(videoplayers)#делит колво серий на колво плееров
        i = 0
        voiceList = list()
        while i < n:
            v= soup.find(id = "sOne" + str(i+1)).get("onclick")
            voiceList.append(v[8:15])
            i =i+1 
        return(voiceList)
    except:
        return('error getVideoVoiced')
    
def getVideoSubtitle(html):#получает Id аниме с субтитрами
    try:
        soup = BeautifulSoup(html, "lxml")
        num = soup.find_all(class_ ="sStl")
        videoplayers= soup.find_all(class_ = "svb")
        n = len (num) / len(videoplayers)#делит колво серий на колво плееров
        i = 0
        subtitleList = list()
        while i < n:
            v= soup.find(id = "sTwo" + str(i+1)).get("onclick")
            subtitleList.append(v[8:15])
            i =i+1 
        return(subtitleList)
    except:
        return("error getVideoSubtitle")