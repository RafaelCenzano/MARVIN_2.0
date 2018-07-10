#Imports
from webbrowser import open as webopen # webbrowser to open websites
import essentials # import speak and listen
from calculator import calculator # import calculator code
import webscrape # import webscrape functions
from json import load # import json load


#####################
# File for commands #
#####################


#COMMANDS

class MarvinCommands(Exception): pass
def dataCommands(command):

    if 'open reddit' in command:
        subreddit = command.split(" ")[2:] # split for anything after 'open reddit'
        subreddit_joined = (" ").join(subreddit) # joining anything that was split from after 'open reddit'
        essentials.speak('Opening subreddit ' + subreddit_joined) # saying the subreddit page
        url = ('https://www.reddit.com/r/' + subreddit_joined) # url with reddit page
        webopen(url, new = 2) # open url in browser
        print('Done!')

    elif 'standby' in command:
        essentials.speak('Going on standby')
        raise MarvinCommands # raise exeption so class passes and restarts loop

    elif 'youtube' in command:
        video = command.split(" ")[1:] # split for anything after 'youtube'
        video_joined = (" ").join(video) # joining anything that was split from after 'youtube'
        essentials.speak('Opening first video for ' + video_joined + ' on YouTube')
        webscrape.scrapeYoutube(video_joined)

    elif 'where is' in command:
        location = command.split(" ")[2:] # split for anything after 'where is'
        location_joined = (" ").join(location) # joining anything that was split from after 'where is'
        essentials.speak('Hold on, I will show you where ' + location_joined + ' is.') # saying the location heard
        url = ('https://www.google.nl/maps/place/' + location_joined + '/&amp;') # url with location
        webopen(url, new = 2) # open url in browser
        print('Done!')

    elif command == 'exit' or command == 'quit' or command == 'leave':
        essentials.speak('exiting')
        exit() # leave program

    elif 'open calculator' in command or 'run calculator' in command or command == 'calculator':
        calculator() # run calculator code from calculator.py

    elif command == 'hello' or command == 'hi':
        essentials.speak('Hello')

    elif command == 'send email':
        try:
            with open('marvin/json/data.json', 'r') as listen_data:
                listen_chat_data = load(listen_data)
            if listen_chat_data['listen'] == 0:
                essentials.speak('Who would you like to send this email to?')
                email_recipent = raw_input(': ').lower()
                essentials.speak('What is the subject of the email?')
                email_subject = raw_input(': ')
                essentials.speak('What is the message you would like to send to ' + email_recipent)
                email_body = raw_input(': ')
                essentials.email(email_recipent, email_subject, email_body)
            elif listen_chat_data['listen'] == 1:
                essentials.speak('Who would you like to send this email to?')
                email_recipent = essentials.listen().lower()
                essentials.speak('What is the subject of the email?')
                email_subject = essentials.listen()
                essentials.speak('What is the message you would like to send to ' + email_recipent)
                email_body = essentials.listen()
                essentials.email(email_recipent, email_subject, email_body)
            else:
                essentials.speak('A file is missing data report to issues on github')
                pass
        except essentials.MarvinEmail:
            pass # stop command

    elif 'amazon' in command:
        amazon = command.split(" ")[1:]
        amazon_search = (" ").join(amazon)
        essentials.speak('Searching amazon for ' + amazon_search)
        url = ('https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + amazon_search)
        webopen(url, new = 2)
        print('Done!')