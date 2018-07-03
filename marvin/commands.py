#Imports
import os # to open files
import webbrowser # webbrowser to open websites
import smtplib # smtplib for sending emails
import essentials # import speak and listen
from calculator import calculator # import calculator code
import webscrape


#####################
# File for commands #
#####################


#COMMANDS

class MarvinCommands(Exception): pass
def dataCommands(command):

    if 'open reddit' in command:
        subreddit = command.split(" ")[2:] # split for anything after 'open reddit'
        subreddit_joined = (" ").join(subreddit) # joining anything that was split from after 'where is'
        essentials.speak('Opening subreddit ' + subreddit_joined) # saying the subreddit page
        url = ('https://www.reddit.com/r/' + subreddit_joined) # url with reddit page
        webbrowser.open(url, new = 2) # open url in browser
        print('Done!')

    elif 'standby' in command:
        essentials.speak('Going on standby')
        raise MarvinCommands # raise exeption so class passes and restarts loop

    elif 'youtube' in command:
        video = command.split(" ")[1:] # split for anything after 'youtube'
        video_joined = (" ").join(video) # joining anything that was split from after 'youtube'
        essentials.speak('Opening first video for ' + video_joined)
        webscrape.scrapeYoutube(video_joined)
'''
    elif 'amazon' in command:
        amazon = command.split(" ")[1:]
        amazon_search = (" ").join(amazon)
        essentials.speak('Searching amazon for ' + amazon_search)
        url = ('https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + amazon_search)
        webbrowser.open(url, new = 2)
        url2 = str(webscrape.scrapeAmazon(command))
        print url2
        webbrowser.open(url2, new = 2)
        print('Done!')'''

    elif 'where is' in command:
        location = command.split(" ")[2:] # split for anything after 'where is'
        location_joined = (" ").join(location) # joining anything that was split from after 'where is'
        essentials.speak('Hold on, I will show you where ' + location_joined + ' is.') # saying the location heard
        url = ('https://www.google.nl/maps/place/' + location_joined + '/&amp;') # url with location
        webbrowser.open(url, new = 2) # open url in browser
        print('Done!')

    elif 'exit' in command or 'quit' in command or 'leave' in command:
        essentials.speak('exiting')
        exit() # leave program

    elif 'open calculator' in command or 'run calculator' in command or 'calculator' in command:
        calculator() # run calculator code from calculator.py

    elif 'hello' in command or 'hi' in command:
        essentials.speak('Hello')

