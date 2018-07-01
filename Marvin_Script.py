#Imports
from marvin import commands
from marvin import essentials

# MAIN
while True :
    # core loop this is the part that will be looped to check user wants to keep using voice commands
    # it will always ask the user the prompt below when the while loop goes back to the start
    # part that will run when while loop resets
    essentials.speak('Would you like to do voice commands?')
    beg_input = raw_input(": ")
    # end of part that will run when while loop resets
 
    if beg_input == 'yes': # once recording data is done and marvin completed commands it will restart the loop and ask 'would you like to do voice commands'
        try:
            while 1:
                print('listening for commands')
                data = essentials.listen() #use listen function in Marvin_Commands.py
                commands.dataCommands(data.lower()) # check for command and lower what was just said
        except commands.MarvinCommands: # except and pass to resume stanby
            pass
    elif beg_input == "quit": # if the user just wants to end marvin
        essentials.speak("exiting")
        exit()
    else:
        essentials.speak("would you like to be on standby?")
        standby = raw_input(": ")
        if standby == "yes":
            essentials.speak("Type start to repoen voice commands or quit to exit")
            y_n = raw_input(": ")
            if y_n == "start":
            # NOTE: !important! READ THIS
            # -> exit all the if statements which will bring us back to the beginning of the loop where it will ask 'would you like to do voice commands'
            # by running the 'continue' function you will be able to skip down to the bottom of the while loop and since there is nothing there to run it will loop back to the beginning
                continue
            else:
                essentials.speak("exiting")
                exit() # exit the while loop to end the code session
        else: # user doesn't want to be on standby so end code session
            essentials.speak("exiting")
            exit() # exit code session
    # end of core loop