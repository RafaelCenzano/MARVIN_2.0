#Imports
from bs4 import BeautifulSoup as bs # process html
import requests # to request page url code
import webbrowser # webbrowser to open websites
import time # for pause between requests
from marvin.essentials import speak # import speak and listen
from urllib.parse import urlparse


########################
# File for webscraping #
########################


class Youtube:
    def __init__(self, search_query):
        self.videolist = [] # create empty list
        self.url = ('https://www.youtube.com/results?search_query=' + search_query)# combine url with search query from command
        r = requests.get(self.url) # request page
        page = r.text # formatting
        soup = bs(page, 'html.parser') # parse html
        self.vids = soup.findAll(attrs={'class':'yt-uix-tile-link'}) # search for class yt-uix-tile-link in html from page

    def is_absolute(self, url):
        return bool(urlparse(url).netloc)

    def scrapeYoutube(self, search_query):
        for v in self.vids: #for loop for finding all videos that show up
            if self.is_absolute(v['href']) == True:
                pass
            else:
                tmp = 'https://www.youtube.com' + v['href'] # create url to add to list with links from html
                self.videolist.append(tmp) # add the newly created url to list
        webbrowser.open(self.videolist[0], new = 2) # open the url
        print('Done!') # finish message

class Tomatoe:
    def __init__(self, search_query):
        self.url = ('https://www.rottentomatoes.com/m/' + search_query_with_under_scores)# combine url with search query from command
        spliting = search_query.split(" ")[0:]
        search_query_with_under_scores = ("_").join(spliting)
        r = requests.get(url) # request page
        page = r.text # formatting
        self.soup = bs(page, 'html.parser') # parse html


    def scrapeRottentomatoes(self):
        rt = self.soup.findAll('span', attrs={'class':'meter-value superPageFontColor'}) # search for class meter-value superPageFontColor in html from page
        try:
            if rt == []: raise Exception
            raiting = rt[0].getText()
            speak('Rotten Tomatoes gave '+ search_query + ' ' + raiting)
            people_score = self.soup.findAll('span', attrs={'class':'superPageFontColor', 'style':'vertical-align:top'})
            score = people_score[0].getText()
            want_or_like = self.soup.findAll('div', attrs={'class':'smaller bold hidden-xs superPageFontColor'})
            like_or_want = want_or_like[0].getText()
            if like_or_want == 'liked it':
                speak('\n' + score + ' of people liked ' + search_query)
            elif like_or_want == 'want to see':
                speak('\n' + score + ' want to see ' + search_query)
            else:
                print('\nError\nI web scraped the wrong data or Rotten Tomatoes changed their format please report this issue immediatly so we can fix it')
        except Exception as e:
            speak('\nI ran into a problem\nThe name of the movie was probably input incorrectly')
            print(e)

    def IMDb(self):
        pg_up = self.soup.findAll('li', attrs={'class':'meta-row clearfix'})
        try:
            if pg_up == []: raise Exception
            up_pg = pg_up[0].getText()
            speak('\n' + search_query + ' got a IMDb' + up_pg)
        except Exception as e:
            speak('\nI ran into a problem\nThe name of the movie was probably input incorrectly')

def getVersion():
    url = ('https://github.com/SavageCoder77/MARVIN_2.0/blob/master/marvin/json/marvin_version.txt')
    r = requests.get(url) # request page
    page = r.text
    soup = bs(page, 'html.parser') # parse html
    vids = soup.findAll('td', attrs={'id':'LC1', 'class':'blob-code blob-code-inner js-file-line'}) # search for class meter-value superPageFontColor in html from page
    version_marvin = vids[0].getText()
    print('Marvin Version ' + str(version_marvin))
    return version_marvin