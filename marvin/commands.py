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

    elif 'hello' in command:
        essentials.speak('Hello')

    elif 'standby' in command:
        essentials.speak('Going on standby')
        raise MarvinCommands # raise exeption so class passes and restarts loop

    elif 'youtube' in command:
        video = command.split(" ")[1:] # split for anything after 'youtube'
        video_joined = (" ").join(video) # joining anything that was split from after 'youtube'
        webscrape.scrapeYoutube(video_joined)

    elif 'where is' in command:
        location = command.split(" ")[2:] # split for anything after 'where is'
        location_joined = (" ").join(location) # joining anything that was split from after 'where is'
        essentials.speak('Hold on, I will show you where ' + location_joined + ' is.') # saying the location heard
        url = ('https://www.google.nl/maps/place/' + location_joined + '/&amp;') # url with location
        webbrowser.open(url, new = 2) # open url in browser
        print('Done!')

    elif 'exit' in command or 'quit' in command:
        essentials.speak('exiting')
        exit() # leave program

    elif 'open calculator' in command or 'run calculator' in command or 'calculator' in command:
        calculator() # run calculator code from calculator.py

