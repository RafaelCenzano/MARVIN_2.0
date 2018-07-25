# Imports
from os import system, path
from time import sleep as wait
from threading import Thread
from json import load, dump
from codecs import encode
from hashlib import sha512
import essentials
import webscrape

###############################
# File for miscellaneous code #
###############################

def ADMIN(contact_path, pass_path):
    while True:
        print('\nOnly use ADMIN acount for administrative tasks')
        print('\n######## ADMIN MENU ########\n\n1. Create New User\n2. Delete a User\n3. Update Marvin\n4. Leave ADMIN Menu\n5. Exit program')
        ADMIN_input = raw_input('>')
        if ADMIN_input == '1' or 'user' in ADMIN_input.lower():
            with open(pass_path, 'r') as login_data:
                new_user_data = load(login_data)
            search_login = new_user_data['logins']
            print('Showing all Users')
            for x in search_login:
                print(x)
            print('You will choose a username and password for the new user\nType a User')
            new_user = raw_input('>')
            if new_user in search_login:
                print('This user exists already')
            else:
                while True:
                    print('\nType a password for the new user thats over 5 characters')
                    new_user_pass = raw_input('>')
                    if len(new_user_pass) <= 5:
                        print('Make your password over 5 characters please')
                    else:
                        break
                new_login = encode(new_user, 'rot13')
                new_user_pass_encrypted = sha512(new_user_pass + new_login).hexdigest()
                print('Creating User')
                with open(pass_path, 'w') as outfile:
                    new_user_data['logins'][new_user] = {"pass":new_user_pass_encrypted}
                    dump(new_user_data, outfile)
                print('New user created')
        elif ADMIN_input == '2' or 'delete' in ADMIN_input.lower():
            with open(pass_path, 'r') as login_data:
                new_user_data = load(login_data)
            search_login = new_user_data['logins']
            print('Showing all Users')
            for x in search_login:
                print(x)
            print('What user do you want to delete')
            del_user = raw_input('>')
            if del_user == 'ADMIN':
                print('Can\'t delete this user')
            elif del_user in search_login:
                while True:
                    print('Type your ADMIN password again to confirm this action')
                    login_pass = raw_input('>')
                    login_pass2 = sha512(login_pass + 'NQZVA').hexdigest()
                    if login_pass2 == new_user_data['logins']['ADMIN']['pass']:
                        break
                    else:
                        print('Incorect Credentials')
                del new_user_data['logins'][del_user]
                with open(pass_path, 'w') as outfile:
                    dump(new_user_data, outfile)
            else:
                print('This User doesn\'t exist')
        elif ADMIN_input == '3' or 'update' in ADMIN_input.lower():
            ('Checking for Update')
            with open('Os.json', 'r') as marvin_v:
                marvin_ver = load(marvin_v)
                marvin_version = marvin_ver['Marvin_Release']
            online_marvin_version = webscrape.getVersion()
            if str(marvin_version) != str(online_marvin_version):
                print('Update found')
                system('git pull')
                print('You will now have to reopen Marvin to make sure the changes went through')
                with open('Os.json', 'w') as outfile:
                    marvin_ver['Marvin_Release'] = online_marvin_version
                    dump(marvin_ver, outfile)
                exit()
            else:
                print('No update found\nYou are up to date')
        elif ADMIN_input == '4' or 'exit' in ADMIN_input.lower() or 'leave' in ADMIN_input.lower() or 'quit' in ADMIN_input.lower():
            print('Exiting ADMIN MENU')
            break
        elif ADMIN_input == '5':
            print('Exiting program')
            exit()

def listofcontacts(contact_list, type_):
    wait(0.7)
    for c in contact_list:
        c_letters = list(c)
        c_letter_first = c_letters[0]
        c_letters_rest = c_letters[1:]
        c_letters_rest_joined = ("").join(c_letters_rest)
        c_letter_first_upper = str(c_letter_first.upper())
        print(c_letter_first_upper + c_letters_rest_joined)
        if type_ != 1:
            email_c = contact_list[c]['email']
            if type_ != 'email':
                phone_c = contact_list[c]['number']
                print('    ' + email_c + '\n    ' + phone_c + '\n')
            else:
                print('    ' + email_c + '\n')

def contactList(contact_path, type_):
    with open(contact_path, 'r') as contact_data_list:
        list_contact_data = load(contact_data_list)
        contact_list = list_contact_data['contacts']
    if not list_contact_data['contacts']:
        print('No contacts use the add contacts command to add some')
    elif not list_contact_data:
        print('Fatal Error\nMissing data make sure that you ran setup.py before running this script')
    else:
        thread_list_contact = Thread(target = listofcontacts, args = (contact_list, type_,))
        thread_list_contact.start()
        essentials.speak('Opening contact list for you now\n')

calculator_path = path.join('marvin','calculator.py')
def openCalculator():
    system('python2.7 ' + calculator_path)
