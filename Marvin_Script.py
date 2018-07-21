# Imports
from marvin import commands
from marvin import essentials
from json import load
from codecs import encode
from hashlib import sha512
import os


# LOGIN
contact_path = os.path.join('marvin','json','contacts.json')
pass_path = os.path.join('marvin','json','pass.json')

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
                login_usr = raw_input('>')
                if login_usr not in search_login:
                    print('\n##############\nIncorrect User\n##############\n')
                else:
                    break
            new_login = encode(login_usr, 'rot13')
            print('Please Type Password')
            login_pass = raw_input('>')
            login_pass2 = sha512(login_pass + new_login).hexdigest()
            if login_pass2 == new_login_data['logins'][login_usr]['pass']:
                if login_usr == 'ADMIN':
                    essentials.ADMIN(contact_path, pass_path)
                break
            else:
                print('\n#####################\nIncorrect Credentials\n#####################\n')
        # MAIN
        while True:
        # core loop this is the part that will be looped to check user wants to keep using voice commands
        # it will always ask the user the prompt below when the while loop goes back to the start
        # part that will run when while loop resets
            essentials.speak('Choose an option')
            print(' \nOPTIONS:\n1. voice commands\n2. chat commands\n3. standby\n4. quit\n ')
            beg_input = raw_input(">")
        # end of part that will run when while loop resets

            if beg_input == '1' or 'voice' in beg_input: # once recording data is done and marvin completed commands it will restart the loop and ask 'would you like to do voice commands'
                try:
                    while 1:
                        print('Awaiting commands')
                        data = essentials.listen() #use listen function in commands.py
                        commands.dataCommands(data.lower(), 1, pass_path, contact_path) # check for command and lower what was just said
                except commands.MarvinCommands: # except and pass to resume stanby
                    pass # restart loop
            elif beg_input == '2' or 'chat' in beg_input:
                try:
                    while 1:
                        print('Awaiting commands')
                        data = raw_input('')
                        commands.dataCommands(data.lower(), 0, pass_path, contact_path) # check for command and lower what was just said and adds 0 value to show raw input and not talking commands
                except commands.MarvinCommands: # except and pass to resume stanby
                    pass #restart loop
            elif beg_input == '3' or 'standby' in beg_input: # standby no recording
                essentials.speak("Type start to reopen commands or quit to exit")
                y_n = raw_input('>')
                if 's' in y_n:
                    pass # restart loop
                else:
                    essentials.speak('exiting')
                    exit() # exit program
            elif beg_input == '4' or 'quit' in beg_input or 'exit' in beg_input: # if the user just wants to end marvin
                essentials.speak('closing program')
                exit() # exit program
            else:
                print('Did you spell it wrong? try again')
    except commands.MarvinRelog:
        pass
# end of core loop