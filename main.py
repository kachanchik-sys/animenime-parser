from os import wait, write
from bs4 import BeautifulSoup
import requests
#from search import generatorURL,getHTML,getInfo,getTitle,getHref,anime_count
import search
import pagePars
import sibnet_parse
import urllib

search_name = "Школа мертвецов"
i = 1

try:
    URL = search.generatorURL(search_name)
    HTML = search.getHTML(URL)
    Info = search.getInfo(HTML)
    TitleList = search.getTitle(Info)
    HrefList = search.getHref(Info)
    count = search.anime_count(HrefList)
    aniHTML = pagePars.getHTML(HrefList[i])
    photo = pagePars.getPhoto(aniHTML)
    description = pagePars.getDescription(aniHTML)
    block_status = pagePars.checkBlock(aniHTML)
    voice = pagePars.getVideoVoiced(aniHTML)
    subtitle = pagePars.getVideoSubtitle(aniHTML)
except IndexError:
    print (f"you enter wrong number of anime. you can enter number in range (0 - {count-1})")
    quit()





if block_status == True:
    print ("this anime is blocked on website ")
    quit()
else:
    sibHTML = sibnet_parse.getHTML(subtitle[0])
    src = sibnet_parse.getSrc(sibHTML)
    

print(photo)
print(HrefList[i])
print(TitleList[i])
print(description)
print(f"number of episodes {len(subtitle)}")
print(src)
#print(voice[i])
#print(subtitle[0])
