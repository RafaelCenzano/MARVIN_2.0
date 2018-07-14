#Imports
from webbrowser import open as webopen # webbrowser to open websites
import essentials # import speak and listen
import webscrape # import webscrape functions
from json import load, dump # import json load
import threading


#####################
# File for commands #
#####################


#COMMANDS

class MarvinCommands(Exception): pass
def dataCommands(command, type_of_input):


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

    elif 'time in' in command:
        time_in = command.split(" ")[2:]
        time_in_location = (" ").join(time_in)
        essentials.speak('Showing time in '+ time_in_location)
        url = ('https://time.is/' + time_in_location)
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

    elif command == 'add contact' or command == 'new contact':
        try:
            print('input cancel to cancel add contact')
            essentials.speak('Who would you like to add to you contacts?')
            add_contact = essentials.commandInput(type_of_input)
            if 'quit' == add_contact or 'exit' == add_contact or'cancel' == add_contact: raise ValueError
            print('input cancel to cancel add contact')
            essentials.speak('What is ' + add_contact + '\'s email?')
            new_email = essentials.commandInput(type_of_input)
            if 'quit' == new_email or 'exit' == new_email or 'cancel' == new_email: raise ValueError
            print('input cancel to cancel add contact')
            essentials.speak('What is ' + add_contact + '\'s phone number? If you don\'t have it or you dont want to input respond with None')
            new_phone_number = essentials.commandInput(type_of_input)
            if 'quit' == new_phone_number or 'exit' == new_phone_number or 'cancel' == new_phone_number: raise ValueError
            essentials.speak('Creating contact')
            with open('marvin/json/contacts.json', 'r') as contact_data:
                new_contact_data = load(contact_data)
            with open('marvin/json/contacts.json', 'w') as outfile:
                new_contact_data['contacts'][add_contact] = {"email":new_email, "number":new_phone_number}
                dump(new_contact_data, outfile)
            print('Contact Created!')
        except Exception as e:
            print('cancelling')

    elif command == 'send email':
        try:
            print('input cancel to cancel send email')
            essentials.speak('Who would you like to send this email to?')
            email_recipient = essentials.commandInput(type_of_input)
            if 'quit' == email_recipient or 'exit' == email_recipient or 'cancel' == email_recipient: raise ValueError
            print('input cancel to cancel send email')
            essentials.speak('What is the subject of the email?')
            email_subject = essentials.commandInput(type_of_input)
            if 'quit' == email_subject or 'exit' == email_subject or 'cancel' == email_subject: raise ValueError
            print('input cancel to cancel send email')
            essentials.speak('What is the message you would like to send to ' + email_recipient)
            email_body = essentials.commandInput(type_of_input)
            if 'quit' == email_body or 'exit' == email_body or 'cancel' == email_body: raise ValueError
            thread_email = threading.Thread(target = essentials.email, args = (email_recipient, email_subject, email_body))
            thread_email.start()
        except Exception as e:
            print('cancelling')

    # Misc Commands #

    elif command == 'open calculator' or command == 'run calculator' or command == 'calculator':
        thread_calculator = threading.Thread(target = essentials.openCalculator) # run calculator code from calculator.py
        print('Calculator Opened!')
        thread_calculator.start()

    elif command == 'hello' or command == 'hi':
        essentials.speak('Hello!')