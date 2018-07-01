#Imports
from bs4 import BeautifulSoup as bs # process html
import requests # to request page url code
import webbrowser # webbrowser to open websites


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

def scrapeAmazon(data):
    url = ('https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + data)
    r = requests.get(url)
    page = r.text
    amazon_query_list = []
    soup = bs(page, 'html.parser')
    divTag = soup.findAll("div", {"class": "s-item-container"})
    for tag in divTag:
        aTags = tag.find_all("a", {"class": "a-link-normal a-text-normal"})
      # New version without looping
      #a_tag = tag.findAll("a", {"class": "a-link-normal a-text-normal"}) # To get the first a tag only
        #link = Atag["href"]
        print (aTags)
        amazon_query_list.append(aTags)
      # This is good but you can find the element with out looping it all
      # divTag2 = tag.find_all("div", {"class": "a-row a-spacing-small"}) # soup.find_all("div", {"class": "a-row a-spacing-small"})
      # for tag in divTag2:
      # tdTags = tag.find_all("a", {"class": "a-link-normal"})
      # for tag in tdTags:
      # tmp = tag['href']
      # amazon_query_list.append(tmp)
    print (amazon_query_list)
    amazon_returned = amazon_query_list[0]
    return amazon_returned