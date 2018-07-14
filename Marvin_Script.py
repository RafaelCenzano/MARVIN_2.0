# Imports
from marvin import commands
from marvin import essentials

# MAIN
while True :
    # core loop this is the part that will be looped to check user wants to keep using voice commands
    # it will always ask the user the prompt below when the while loop goes back to the start
    # part that will run when while loop resets
    essentials.speak('Would you like to do voice commands, chat commands, or be on standby?')
    print(' \nOPTIONS:\n1. voice commands\n2. chat commands\n3. standby\n4. quit\n ')
    beg_input = raw_input(": ")
    # end of part that will run when while loop resets
 
    if beg_input == '1' or 'voice' in beg_input: # once recording data is done and marvin completed commands it will restart the loop and ask 'would you like to do voice commands'
        try:
            while 1:
                print('Awaiting commands')
                data = essentials.listen() #use listen function in commands.py
                commands.dataCommands(data.lower(), 1) # check for command and lower what was just said
        except commands.MarvinCommands: # except and pass to resume stanby
            pass # restart loop
    elif beg_input == '2' or 'chat' in beg_input:
        try:
            while 1:
                print('Awaiting commands')
                data  = raw_input('')
                commands.dataCommands(data.lower(), 0) # check for command and lower what was just said and adds 0 value to show raw input and not talking commands
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
# end of core loop