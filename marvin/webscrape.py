#Imports
from bs4 import BeautifulSoup as bs # process html
import requests # to request page url code
import webbrowser # webbrowser to open websites


########################
# File for webscraping #
########################

def scrapeYoutube(data):
    url = ('https://www.youtube.com/results?search_query=' + data)
    r = requests.get(url)
    page = r.text
    soup = bs(page, 'html.parser')
    vids = soup.findAll(attrs={'class':'yt-uix-tile-link'})
    videolist=[]
    for v in vids:
        tmp = 'https://www.youtube.com' + v['href']
        videolist.append(tmp)
    watchurl = videolist[0]
    webbrowser.open(watchurl, new = 2)
