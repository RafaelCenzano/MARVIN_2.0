# Imports
import os
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
os_release = release()
print ('Decting Operating System')
print ('Your os type is ' + check_os)
print ('Your os version is ' + os_release)

print('Creating needed files')

contacts_path = os.path.join('marvin','json','contacts.json')
pass_path = os.path.join('marvin','json','pass.json')

print('We need your email to be able to send emails')
print('\n#####\nYou will need to change an email setting that allows less secure apps\n#####\n')
print('\nIf you dont want the email function type none')
print('Please type email address')
email_usr = raw_input('>')
print('Please type email password')
email_pass = raw_input('>')

try:
    with open('Os.json', 'w') as outfile:
        var2 = {"Marvin_Release":"0.0.2","Os_data":{"OS":check_os,"os_release":os_release}}
        dump(var2, outfile)
    with open(contacts_path, 'w') as outfile1:
        var = {"contacts":{},"nicks":{}}
        dump(var, outfile1)
    with open(pass_path, 'w') as outfile2:
        var1 = {"email_address":email_usr, "email_password":email_pass, "logins":{"ADMIN":{"pass":pass_new}}}
        dump(var1, outfile2)
except Exception as e:
    print('We ran into a problem\nPlease report this issue ' + str(e) + '\nFiles couldn\'t be created properly')

if check_os == 'Linux':
    try:
        print('\nGoing to install tkinter for GUI')
        os.system('sudo apt-get install python-tk')
    except Exception as e:
        print('We ran into a problem\nPlease report this issue ' + str(e))
        
elif check_os == 'Darwin':
    try:
        print('We need to install Homebrew so that we can install portaudio')
        os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
        print('Installing portaudio')
        os.system('brew install portaudio')
    except Exception as e:
        print('We ran into a problem\nPlease report this issue ' + str(e))
elif check_os == 'Windows': pass
else:
    print ('We dont have a way to set up Marvin on your Operating System.\nIf this is a mistake make sure to report it as an issue at https://github.com/SavageCoder77/MARVIN_2.0')
os.system('pip install -r requirements.txt')
print('\n\nAll files and installs completed\nYou can now run Marvin with Marvin_Script.py')
