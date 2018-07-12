#Imports
from webbrowser import open as webopen # webbrowser to open websites
import essentials # import speak and listen
from calculator import calculator # import calculator code
import webscrape # import webscrape functions
from json import load, dump # import json load
import threading


#####################
# File for commands #
#####################


#COMMANDS

class MarvinCommands(Exception): pass
def dataCommands(command):


    # Website Commands #

    if 'open reddit' in command:
        subreddit = command.split(" ")[2:] # split for anything after 'open reddit'
        subreddit_joined = (" ").join(subreddit) # joining anything that was split from after 'open reddit'
        essentials.speak('Opening subreddit ' + subreddit_joined) # saying the subreddit page
        url = ('https://www.reddit.com/r/' + subreddit_joined) # url with reddit page
        webopen(url, new = 2) # open url in browser
        print('Done!')

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

    elif 'amazon' in command:
        amazon = command.split(" ")[1:]
        amazon_search = (" ").join(amazon)
        essentials.speak('Searching amazon for ' + amazon_search)
        url = ('https://www.amazon.com/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords=' + amazon_search)
        webopen(url, new = 2)
        print('Done!')

    # Marvin Function Commands #

    elif 'standby' in command:
        essentials.speak('Going on standby')
        raise MarvinCommands # raise exeption so class passes and restarts loop

    elif command == 'exit' or command == 'quit' or command == 'leave':
        essentials.speak('exiting')
        exit() # leave program

    # Sending based Commands

    elif command == 'add contact':
        try:
            with open('marvin/json/data.json', 'r') as listen_data:
                listen_chat_data = load(listen_data)
            if listen_chat_data['listen'] == 0:
                print('input cancel to cancel add contact')
                essentials.speak('Who would you like to add to you contacts?')
                add_contact = raw_input(': ')
                if 'quit' 'exit' 'cancel' in add_contact: raise ValueError
                print('input cancel to cancel add contact')
                essentials.speak('What is ' + add_contact + '\'s email?')
                new_email = raw_input(': ')
                if 'quit' 'exit' 'cancel' in new_email: raise ValueError
                print('input cancel to cancel add contact')
                essentials.speak('What is ' + add_contact + '\'s phone number?')
                essentials.speak('If you don\'t have it or you dont want to input respond with None')
                new_phone_number = raw_input(': ')
                if 'quit' 'exit' 'cancel' in new_phone_number: raise ValueError
                essentials.speak('Creating contact')
                with open('marvin/json/contacts.json', 'r') as contact_data:
                    new_contact_data = load(contact_data)
                with open('marvin/json/contacts.json', 'w') as outfile:
                    new_contact_data['contacts'][add_contact] = {"email":new_email, "number":new_phone_number}
                    dump(new_contact_data, outfile)
                print('Done!')
            elif listen_chat_data['listen'] == 1:
                essentials.speak('Who would you like to add to you contacts?')
                add_contact = essentials.listen()
                if 'quit' 'exit' 'cancel' in new_phone_number: raise ValueError
                print('input cancel to cancel add contact')
                essentials.speak('What is ' + add_contact + '\'s email?')
                new_email = essentials.listen()
                if 'quit' 'exit' 'cancel' in new_phone_number: raise ValueError
                print('input cancel to cancel add contact')
                essentials.speak('What is ' + add_contact + '\'s phone number?')
                essentials.speak('If you don\'t have it or you dont want to input respond with None')
                new_phone_number = essentials.listen()
                if 'quit' 'exit' 'cancel' in new_phone_number: raise ValueError
                essentials.speak('Creating contact')
                with open('marvin/json/contacts.json', 'r') as contact_data:
                    new_contact_data = load(contact_data)
                with open('marvin/json/contacts.json', 'w') as outfile:
                    new_contact_data['contacts'][add_contact] = {"email":new_email, "number":new_phone_number}
                    dump(new_contact_data, outfile)
            else:
                essentials.speak('A file is missing data report to issues on github')
                raise Exception
        except Exception as e:
            print('cancelling')

    elif command == 'send email':
        try:
            with open('marvin/json/data.json', 'r') as listen_data:
                listen_chat_data = load(listen_data)
            if listen_chat_data['listen'] == 0:
                print('input cancel to cancel send email')
                essentials.speak('Who would you like to send this email to?')
                email_recipient = raw_input(': ')
                if 'quit' 'exit' 'cancel' in email_recipient: raise ValueError
                email_recipient_lower = email_recipient.lower()
                print('input cancel to cancel send email')
                essentials.speak('What is the subject of the email?')
                email_subject = raw_input(': ')
                if 'quit' 'exit' 'cancel' in email_subject: raise ValueError
                print('input cancel to cancel send email')
                essentials.speak('What is the message you would like to send to ' + email_recipient)
                email_body = raw_input(': ')
                if 'quit' 'exit' 'cancel' in email_body: raise ValueError
                essentials.email(email_recipient_lower, email_subject, email_body)
            elif listen_chat_data['listen'] == 1:
                essentials.speak('Who would you like to send this email to?')
                email_recipient = essentials.listen()
                if 'quit' 'exit' 'cancel' in email_recipient: raise ValueError
                email_recipient_lower = email_recipient.lower()
                essentials.speak('What is the subject of the email?')
                email_subject = essentials.listen()
                if 'quit' 'exit' 'cancel' in email_subject: raise ValueError
                essentials.speak('What is the message you would like to send to ' + email_recipient)
                email_body = essentials.listen()
                if 'quit' 'exit' 'cancel' in email_body: raise ValueError
                essentials.email(email_recipient_lower, email_subject, email_body)
            else:
                essentials.speak('A file is missing data report to issues on github')
                raise Exception
        except Exception as e:
            print('cancelling')

    # Misc Commands #

    elif command == 'open calculator' or command == 'run calculator' or command == 'calculator':
        thread_calculator = threading.Thread(target = calculator) # run calculator code from calculator.py
        thread_calculator.start()

    elif command == 'hello' or command == 'hi':
        essentials.speak('Hello')