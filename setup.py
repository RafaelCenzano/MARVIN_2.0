# Imports
import os
import platform
import json
import hashlib

# Main Code
while True:
    print('Setting Up Marvin\nPlease set a password for the ADMIN acount\nMake the password longer than 5 characters')
    new_pass = raw_input('>')
    if len(new_pass) <= 5:
        print('Make your password longer than 5 characters please')
    else:
        pass_new = hashlib.sha512(new_pass + 'NQZVA').hexdigest()
        break

check_os = platform.system()
print ('Decting Operating System')
print ('Your os name is ' + os.name)
print ('Your os type is ' + check_os)
print ('Your os version is ' + platform.release())

with open('marvin/json/contacts.json', 'w') as outfile1:
    var = {'contacts':{'example':{"email":"email@domain.com","number":"number here"}}}
    json.dump(var, outfile1)
with open('marvin/json/pass.json', 'w') as outfile2:
    var1 = {'logins':{'ADMIN':{"usr":"NQZVA","pass":pass_new}}}
    json.dump(var1, outfile2)

os.system('pip install -r requirements.txt')

if check_os == 'Linux':
    print('Going to install tkinter for GUI')
    os.system('sudo apt-get install python-tk')
elif check_os == 'Darwin':
    print('We need to install Homebrew so that we can install portaudio')
    os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    print('Installing portaudio')
    os.system('brew install portaudio')
elif check_os == 'Windows': pass
else:
    print ('We dont have a way to set up Marvin on your Operating System.\nIf this is a mistake make sure to report it as an issue at https://github.com/SavageCoder77/MARVIN_2.0')
