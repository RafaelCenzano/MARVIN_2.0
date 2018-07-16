# Imports
from os import system, name
from platform import system, release
from json import dump
from hashlib import sha512

# Main Code
while True:
    print('Setting Up Marvin\nADMIN acount username is ADMIN\nPlease set a password for the ADMIN acount\nMake the password longer than 5 characters')
    new_pass = raw_input('>')
    if len(new_pass) <= 5:
        print('Make your password longer than 5 characters please')
    else:
        pass_new = sha512(new_pass + 'NQZVA').hexdigest()
        break

check_os = system()
print ('Decting Operating System')
print ('Your os name is ' + name)
print ('Your os type is ' + check_os)
print ('Your os version is ' + release())

with open('marvin/json/contacts.json', 'w') as outfile1:
    var = {'contacts':{'example':{"email":"email@domain.com","number":"number here"}}}
    dump(var, outfile1)
with open('marvin/json/pass.json', 'w') as outfile2:
    var1 = {'logins':{'ADMIN':{"pass":pass_new}}}
    dump(var1, outfile2)

if check_os == 'Linux':
    print('Going to install tkinter for GUI')
    system('sudo apt-get install python-tk')
elif check_os == 'Darwin':
    print('We need to install Homebrew so that we can install portaudio')
    system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    print('Installing portaudio')
    system('brew install portaudio')
elif check_os == 'Windows': pass
else:
    print ('We dont have a way to set up Marvin on your Operating System.\nIf this is a mistake make sure to report it as an issue at https://github.com/SavageCoder77/MARVIN_2.0')
    exit()

system('pip install -r requirements.txt')
print('\n\nCompleted all downloads')