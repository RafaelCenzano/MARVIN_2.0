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

def scrapeYoutube(search_query):
    url = ('https://www.youtube.com/results?search_query=' + search_query)# combine url with search query from command
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

def scrapeRottentomatoes(search_query):
    split = search_query.split(" ")
    search_query_with_under_scores = ("_").join(split)
    url = ('https://www.rottentomatoes.com/m/' + search_query_with_under_scores)# combine url with search query from command
    r = requests.get(url) # request page
    page = r.text
    soup = bs(page, 'html.parser') # parse html
    vids = soup.findAll('span', attrs={'class':'meter-value superPageFontColor'}) # search for class meter-value superPageFontColor in html from page
    needed = vids[0]
    


scrapeRottentomatoes('Avengers Infinity War')