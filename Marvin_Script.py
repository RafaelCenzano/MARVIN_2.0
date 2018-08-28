# Imports
import marvin.commands
from marvin.essentials import speak, listen
import marvin.admin_menu
from json import load
from codecs import encode
from hashlib import sha512
import os


# LOGIN
contact_path = os.path.join('marvin','json','contacts.json')
pass_path = os.path.join('marvin','json','pass.json')
with open('Os.json', 'r') as os_data:
    os_type_loaded = load(os_data)
    os_type = os_type_loaded['Os_data']['OS']

while True:
    try:
        with open(pass_path, 'r') as login_data:
            new_login_data = load(login_data)
            search_login = new_login_data['logins']
        while True:
            while True:
                print('\n\n\n\n##### LOGIN #####\n')
                print('Login in with:')
                for x in search_login:
                    print(x)
                login_usr = input('>')
                if login_usr not in search_login:
                    print('\n##############\nIncorrect User\n##############\n')
                else:
                    break
            new_login = encode(login_usr, 'rot13')
            print('Please Type Password')
            login_pass = input('>')
            login_pass2 = sha512(login_pass.encode('utf-8') + new_login.encode('utf-8')).hexdigest()
            if login_pass2 == new_login_data['logins'][login_usr]['pass']:
                if login_usr == 'ADMIN':
                    marvin.admin_menu.ADMIN(contact_path, pass_path)
                    raise marvin.commands.MarvinRelog
                break
            else:
                print('\n#####################\nIncorrect Credentials\n#####################\n')
        # MAIN
        while True:
        # core loop this is the part that will be looped to check user wants to keep using voice commands
        # it will always ask the user the prompt below when the while loop goes back to the start
        # part that will run when while loop resets
            speak('\nChoose an option')
            print(' \nOPTIONS:\n1. voice commands\n2. chat commands\n3. standby\n4. quit\n ')
            beg_input = input(">")
        # end of part that will run when while loop resets

            if beg_input == '1' or 'voice' in beg_input: # once recording data is done and marvin completed commands it will restart the loop and ask 'would you like to do voice commands'
                try:
                    while 1:
                        print('\nAwaiting commands')
                        data = listen() #use listen function in commands.py
                        marvin.commands.dataCommands(data.lower(), 1, pass_path, contact_path, os_type) # check for command and lower what was just said
                except marvin.commands.MarvinCommands: # except and pass to resume stanby
                    pass # restart loop
            elif beg_input == '2' or 'chat' in beg_input:
                try:
                    while 1:
                        print('\nAwaiting commands')
                        data = input('')
                        marvin.commands.dataCommands(data.lower(), 0, pass_path, contact_path, os_type) # check for command and lower what was just said and adds 0 value to show raw input and not talking commands
                except marvin.commands.MarvinCommands: # except and pass to resume stanby
                    pass #restart loop
            elif beg_input == '3' or 'standby' in beg_input: # standby no recording
                while True:
                    print("Type start to reopen commands or quit to exit")
                    y_n = input('>')
                    if 'start' in y_n:
                        break # restart loop
                    elif 'quit' in y_n.lower() or 'leave' in y_n.lower() or 'exit' in y_n.lower():
                        speak('exiting')
                        exit() # exit program
                    else:
                        pass
            elif beg_input == '4' or 'quit' in beg_input or 'exit' in beg_input: # if the user just wants to end marvin
                speak('closing program')
                exit() # exit program
            else:
                print('Did you spell it wrong? try again')
    except marvin.commands.MarvinRelog:
        pass
# end of core loop