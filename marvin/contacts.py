# Imports
from time import sleep as wait # to have a pause
from json import load # parse and add json data
from threading import Thread # thread to maximize efficency of marvin
from marvin.essentials import speak # speak to user

##########################
# File for contacts code #
##########################

# Functions

# Function to check contacts
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