#Imports
import Marvin_Commands as marvin

# run the while loop to ask user if they want to do voice commands
while True :
    # core loop this is the part that will be looped to check user wants to keep using voice commands
    # it will always ask the user the prompt below when the while loop goes back to the start
    # part that will run when while loop resets
    marvin.speak('Would you like to do voice commands?')
    beg_input = raw_input(": ")
    # end of part that will run when while loop resets
 
    if beg_input == 'yes':
    # once recording data is done and marvin completed commands it will restart the loop and ask 'would you like to do voice commands'
        while 1:
            print('listening for commands')
            data = marvin.listen()
            marvin.commands(data.lower())
    elif beg_input == "quit": # if the user just wants to end marvin
        marvin.speak("exiting")
        break
    else:
        marvin.speak("would you like to be on standby?")
        standby = raw_input(": ")
    
        if standby == "yes":
            marvin.speak("Type start to repoen voice commands or quit to exit")
            y_n = raw_input(": ")

            if y_n == "start":
            # NOTE: !important! READ THIS
            # -> exit all the if statements which will bring us back to the beginning of the loop where it will ask 'would you like to do voice commands'
            # by running the 'continue' function you will be able to skip down to the bottom of the while loop and since there is nothing there to run it will loop back to the beginning
                continue
            else:
            # break the while loop to end the code session
                break
        else:
        # user doesn't want to be on standby so end code session
            marvin.speak("exiting")
        # exit code session
            exit()
    # end of core loop