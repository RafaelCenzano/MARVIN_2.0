#Imports
from bs4 import BeautifulSoup as bs # process html
import requests # to request page url code
import webbrowser # webbrowser to open websites
import time # for pause between requests
import essentials # import speak and listen
import random # for randomizing random request


########################
# File for webscraping #
########################

def scrapeYoutube(data):
    url = ('https://www.youtube.com/results?search_query=' + data)# combine url with search query from command
    r = requests.get(url) # request page
    page = r.text
    soup = bs(page, 'html.parser') # parse html
    vids = soup.findAll(attrs={'class':'yt-uix-tile-link'}) # search for class yt-uix-tile-link in html from page
    videolist=[] # create empty list
    for v in vids: #for loop for finding all videos that show up
        tmp = 'https://www.youtube.com' + v['href'] # create url to add to list with links from html
        videolist.append(tmp) # add the newly created url to list
    watchurl = videolist[0] # take the first url
    webbrowser.open(watchurl, new = 2) # open the url
    print('Done!')

def requestAmazon(data):
    url = ('https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + data)
    r = requests.get(url)
    page = r.text
    soup = bs(page, 'html.parser')
    return soup

def scrapeAmazon(data):
    while True:
        soup = requestAmazon(data)
        divTag = soup.find_all("div", {"class": "s-item-container"})
        amazon_query_list = []
        if divTag != []:
            for tag in divTag:
                aTags = tag.find_all("a", {"class": "a-link-normal a-text-normal"})
                amazon_query_list.append(aTags)
            amazon_returned = amazon_query_list[1]
            return amazon_returned
            break
        else:
            essentials.speak('I ran into a problem will retry to fix the issue')
            time.sleep(0.9)
            rand_request = ['monitor','mice','python book','drone','rc car','rc helicopter','java book','javascript book','usb drives','usb hub','dog toys','cat toys','laptop','gaming laptop','headphones','gaming headphones']
            requestAmazon(random.choice(rand_request))
            time.sleep(0.5)
            print('Almost there')
            time.sleep(1.3)
            continue