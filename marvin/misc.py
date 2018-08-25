# Imports
from os import system, path # for getting paths for any os and system for running terminal commands
from time import sleep as wait # to have a pause
from json import load, dump # parse and add json data
from codecs import encode # to create new passwords
from socket import socket, AF_INET, SOCK_DGRAM # import socket to get ip address
from hashlib import sha512 # to create new passwords
from platform import system # find os type
from threading import Thread # thread to maximize efficency of marvin
#import essentials
#from webscrape import getVersion # webscrape version
from essentials import speak # speak to user
from subprocess import Popen, PIPE # to run GUI with terminal command

###############################
# File for miscellaneous code #
###############################

# Functions

# Function to get ip of local device on network no 127.0.0.1
def get_ip():
    s = socket(AF_INET, SOCK_DGRAM) # defining socket
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1)) # connect
        IP = s.getsockname()[0] # get ip
    except: # when no ip found
        IP = '127.0.0.1' # local ip to return if no ip found
    finally: # at end of code
        s.close() # close connection
    return IP # return that was found

# Function to show ADMIN Menu
def ADMIN(contact_path, pass_path): # ADMIN MENU
    while True: # loop for MENU so you don't have to keep reopening it
        print('\nOnly use ADMIN acount for administrative tasks') # message to remind you can't use marvins command without a real user
        print('\n######## ADMIN MENU ########\n\n1. Create New User     2. Delete a User\n3. Update Marvin       4. Marvin APPS\n5. Leave ADMIN Menu    6. Exit program') # show options
        ADMIN_input = raw_input('>') # prompt for input

        if ADMIN_input == '1' or 'user' in ADMIN_input.lower(): # check if user wants to create a user
            with open(pass_path, 'r') as login_data: # open user info
                new_user_data = load(login_data) # parse user info
            search_login = new_user_data['logins'] # put users into variable
            print('Showing all Users') # print user printing user message
            for x in search_login: # loop for all users
                print(x) # print all users
            print('You will choose a username and password for the new user\nType a User') # prompt for new usr and pass
            new_user = raw_input('>') # type user
            if new_user in search_login: # check if user exists
                print('This user exists already') # user exists message
            else: # user doesn't exist
                while True: # loop until password over 5 characters
                    print('\nType a password for the new user thats over 5 characters') # message that pass have to be over 5 length
                    new_user_pass = raw_input('>') # input for new user pass
                    if len(new_user_pass) <= 5: # if new password under 5 characters
                        print('Make your password over 5 characters please') # more characters message
                    else: # password over 5 characters
                        break # break loop
                while True: # loop until correct passward
                    print('\nType your ADMIN password again to confirm this action') # ask for admin password
                    login_pass = raw_input('>') # input password
                    login_pass2 = sha512(login_pass + 'NQZVA').hexdigest() # hash password to match if in file
                    if login_pass2 == new_user_data['logins']['ADMIN']['pass']: # check if password matches
                        break # leave loop
                    else: # password doesn't match
                        print('Incorect Credentials') # wrong password message
                        i = i + 1 # add tries
                        if i >= 5: # if over 5 tries
                            exit() # exit
                new_login = encode(new_user, 'rot13') # encode user name
                new_user_pass_encrypted = sha512(new_user_pass + new_login).hexdigest() # hash password
                print('Creating User') # print creating messsage
                with open(pass_path, 'w') as outfile: # open file to add changes
                    new_user_data['logins'][new_user] = {"pass":new_user_pass_encrypted} # new user data
                    dump(new_user_data, outfile) # add new user data
                print('New user created') # new user added messgae

        elif ADMIN_input == '2' or 'delete' in ADMIN_input.lower(): # check if user wants to delete a user
            with open(pass_path, 'r') as login_data: # open file to find exisiting users
                new_user_data = load(login_data) # parse data
            search_login = new_user_data['logins'] # get all users
            print('Showing all Users') # showing users message
            for x in search_login: # loop until all users printed
                print(x) # print all users
            print('\nWhat user do you want to delete') # ask which user to delete
            del_user = raw_input('>') # input for user to delete
            if del_user == 'ADMIN': # if input user is ADMIN
                print('Can\'t delete this user') # can't delete message
            elif del_user in search_login: # check if user exists
                while True: # loop until correct passward
                    print('\nType your ADMIN password again to confirm this action') # ask for admin password
                    login_pass = raw_input('>') # input password
                    login_pass2 = sha512(login_pass + 'NQZVA').hexdigest() # hash password to match if in file
                    if login_pass2 == new_user_data['logins']['ADMIN']['pass']: # check if password matches
                        break # leave loop
                    else: # password doesn't match
                        print('Incorect Credentials') # wrong password message
                        i = i + 1 # add tries
                        if i >= 5: # if over 5 tries
                            exit() # exit
                del new_user_data['logins'][del_user] # del user and data
                with open(pass_path, 'w') as outfile: # open file
                    dump(new_user_data, outfile) # add updated file
            else: # no user found 
                print('This User doesn\'t exist') # no user found message

        elif ADMIN_input == '3' or 'update' in ADMIN_input.lower(): # check if user want to update
            ('Checking for Update') # checking message
            with open('Os.json', 'r') as marvin_v: # open .Os.json to see marvin version
                marvin_ver = load(marvin_v) # parse data
                marvin_version = marvin_ver['Marvin_Release'] # get local marvin version
            online_marvin_version = getVersion() # get online marvin version
            if str(marvin_version) != str(online_marvin_version): # if they don't match
                print('Update found') # found message
                system('git pull') # pull from github
                print('You will now have to reopen Marvin to make sure the changes went through') # restart message
                with open('Os.json', 'w') as outfile: # open .Os.json to change marvin version
                    marvin_ver['Marvin_Release'] = online_marvin_version # change marvin version
                    dump(marvin_ver, outfile) # add new version number
                exit() # exit to restart
            else: # versions match
                print('No update found\n##############\nYou are up to date') # versions match message

        elif ADMIN_input == '4' or 'app' in ADMIN_input:
            print('\nshowing apps:\n')
            with open('Os.json', 'r') as marvin_a: # open .Os.json to see marvin version
                marvin_apps = load(marvin_a) # parse data
            print('IOS app : ' + marvin_apps['apps']['IOS'])
            print('\nWould you like to enable any apps?')
            app_input = raw_input('>').lower()
            if app_input == 'yes' or 'y' in app_input:
                print('\nWhich app would you like to activate')
                app_active = raw_input('>').lower()
                if app_active == 'ios' or app_active == 'apple':
                    get_ip()

        elif ADMIN_input == '5' or 'exit' in ADMIN_input.lower() or 'leave' in ADMIN_input.lower() or 'quit' in ADMIN_input.lower(): # check if user wants to leave Menu
            print('Exiting ADMIN MENU') # exit menu message
            break # break loop to leave ADMIN MENU

        elif ADMIN_input == '6': # if you want to exit
            print('Exiting program') # exit message
            exit() # close program

def checkcontact(contact_path, name):
    with open(contact_path, 'r') as check_name:
        name_check = load(check_name)
    name_low = name.lower()
    if name_low in name_check['contacts']:
        return name
    elif name_low in name_check['nicks']:
        real_name = ['nicks'][name_low]['real_name']
        return real_name
    else:
        return 'None'

# Function to show contacts with variables to determine what extra information to show
def listofcontacts(contact_list, type_):
    wait(0.7) # delay so it starts speaking first
    for c in contact_list: # loop for however many contacts
        c_letters = list(c) # break contacts into letters
        c_letter_first = c_letters[0] # get first letter 
        c_letters_rest = c_letters[1:] # get all other letters
        c_letters_rest_joined = ("").join(c_letters_rest) # join all other letters back into a word
        c_letter_first_upper = str(c_letter_first.upper()) # make the first letter uppercase
        print(c_letter_first_upper + c_letters_rest_joined) # print the uppercase letter and rest of name to look like normal name
        if type_ != 1: # if this doesn't need contact data
            email_c = contact_list[c]['email'] # get email of contact
            if type_ != 'email': # if you want phone and email
                phone_c = contact_list[c]['number'] # get phone numbers
                print('    ' + email_c + '\n    ' + phone_c + '\n') # print email and phone
            else: # only email
                print('    ' + email_c + '\n') # print only email

# Function to open contact file and help sort for what information needed from listofcontacts()
def contactList(contact_path, type_):
    with open(contact_path, 'r') as contact_data_list: # get contact data
        list_contact_data = load(contact_data_list) # parse contact data
        contact_list = list_contact_data['contacts'] # put all contacts in variable
    if not list_contact_data['contacts']: # if no contacts
        print('No contacts use the add contacts command to add some') # no contact message
    elif not list_contact_data: # missing file and data
        print('Fatal Error\nMissing data make sure that you ran setup.py before running this script') # missing file and data message
    else: # there are contacts and there was a file
        thread_list_contact = Thread(target = listofcontacts, args = (contact_list, type_,)) # thread arguments to print list while speaking because of slow speak times
        thread_list_contact.start() # start thread of lisofcontacts function
        speak('Opening contact list for you now\n') # speak

# Function to open calculator GUI with subprocess
def openCalculator():
    if system() == 'Windows':
        python_path = path.join('marvin-env','Scripts','python.exe')
    else:
        python_path = path.join('marvin-env','bin','python2.7') # get path for any os
    calculator_path = path.join('marvin','calculator.py') # get path for any os
    calculator = Popen([python_path + ' ' + calculator_path], stdout = PIPE, stderr = PIPE, shell = True) # terminal command to run in shell
    (out, err) = calculator.communicate() # opening calculator file

# Function to open Stopwatch GUI with subprocess
def openStopwatch():
    if system() == 'Windows': # For windows os
        python_path = path.join('marvin-env','Scripts','python.exe') # executable for windows
    else: # for linux and unix
        python_path = path.join('marvin-env','bin','python2.7') # get path for any os
    stopwatch_path = path.join('marvin','stopwatch.py') # get path for any os
    stopwatch = Popen([python_path + ' ' + stopwatch_path], stdout = PIPE, stderr = PIPE, shell = True) # terminal command to run in shell
    (out, err) = stopwatch.communicate() # opening stopwatch file

if __name__ == '__main__':
    print(get_ip()) # test