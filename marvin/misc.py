# Imports
import socket # import socket to get ip address
from platform import system # find os type
from subprocess import Popen, PIPE # to run GUI with terminal command

###############################
# File for miscellaneous code #
###############################

# Functions

# Function to get ip of local device on network no 127.0.0.1
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # defining socket
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1)) # connect
        IP = s.getsockname()[0] # get ip
    except: # when no ip found
        IP = '127.0.0.1' # local ip to return if no ip found
    finally: # at end of code
        s.close() # close connection
    return IP # return that was found

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
