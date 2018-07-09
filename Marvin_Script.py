# Imports
from marvin import commands
from marvin import essentials
from json import dump

# MAIN
while True :
    # core loop this is the part that will be looped to check user wants to keep using voice commands
    # it will always ask the user the prompt below when the while loop goes back to the start
    # part that will run when while loop resets
    essentials.speak('Would you like to do voice commands, chat commands, or be on standby?')
    print('1. voice commands\n2. chat commands\n3. standby\n4. quit\n ')
    beg_input = raw_input(": ")
    # end of part that will run when while loop resets
 
    if beg_input == '1' or 'voice' in beg_input: # once recording data is done and marvin completed commands it will restart the loop and ask 'would you like to do voice commands'
        try:
            with open('marvin/json/data.json', 'w') as outfile:
                listen_data['listen'] = 1
                dump(listen_data, outfile)
            while 1:
                print('listening for commands')
                data = essentials.listen() #use listen function in commands.py
                commands.dataCommands(data.lower()) # check for command and lower what was just said
        except commands.MarvinCommands: # except and pass to resume stanby
            with open('marvin/json/data.json', 'w') as outfile:
                listen_data['listen'] = 0
                dump(listen_data, outfile)
            pass # restart loop
    elif beg_input == '4' or 'quit' in beg_input or 'exit' in beg_input: # if the user just wants to end marvin
        essentials.speak('closing program')
        exit() # exit program
    elif beg_input == '2' or 'chat' in beg_input:
        try:
            with open('marvin/json/data.json', 'w') as outfile:
                listen_data['listen'] = 0
            while 1:
                print('Awaiting commands')
                data  = raw_input(': ')
                commands.dataCommands(data.lower()) # check for command and lower what was just said
        except commands.MarvinCommands: # except and pass to resume stanby
            pass #restart loop
    elif beg_input == '3' or 'standby' in beg_input: # standby no recording
        essentials.speak("Type start to reopen commands or quit to exit")
        y_n = raw_input(": ")
        if 's' in y_n:
            pass # restart loop
        else:
            essentials.speak('exiting')
            exit() # exit program
    else:
        print('Did you spell it wrong? try again')
        pass # restart loop
# end of core loop