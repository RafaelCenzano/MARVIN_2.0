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

path = os.getcwd()
def unix_linux():
    os.system('chmod 755 .installs.sh')
    os.system('./.installs.sh')
    os.system('chmod 755 marvin/rest-server/start_rest.sh')
    os.system('chmod 755 marvin_run.sh')
    env = ('source ' + path + '/marvin-env/bin/activate')
    script = (path + '/marvin-env/bin/python2.7 ' + path + '/Marvin_Script.py')
    cd = ('cd ' + path)
    out2 = open('marvin_run.sh', 'a')
    out3.write('#!/bin/bash')
    out2.write('\n')
    out2.write(env)
    out2.write('\n')
    out2.write(cd)
    out2.write('\n')
    out2.write(script)
    out2.write('\n')
    out2.write('deactivate')
    out2.close()
    script2 = (path + '/marvin-env/bin/python2.7 ' + path + '/marvin/rest-server/rest-server.py')
    cd2 = ('cd ' + path + '/marvin/rest-server')
    out3 = open('marvin/rest-server/start_rest.sh', 'a')
    out3.write('#!/bin/bash')
    out3.write('\n')
    out3.write(env)
    out3.write('\n')
    out3.write(cd2)
    out3.write('\n')
    out3.write(script2)
    out3.write('\n')
    out3.write('deactivate')
    out3.close()

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
    with open('.Os.json', 'w') as outfile:
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

print('Start installs')
os.system('pip install virtualenv')
os.system('virtualenv marvin-env')

if check_os == 'Linux':
    alias = 'alias marvin="' + path + '/marvin_run.sh"'
    homefolder = os.path.expanduser('~')
    bashrc = os.path.abspath('%s/.bashrc' % homefolder)
    with open(bashrc, 'r') as f:
        lines = f.readlines()
        if alias in lines:
            print('Please delete your alias command marvin in your .bashrc file')
            exit()
        else:
            out = open(bashrc, 'a')
            out.write(alias)
            out.close()
    os.system('source ' + bashrc)
    print('\nGoing to install tkinter for GUI')
    os.system('sudo apt-get install python-tk')

elif check_os == 'Darwin':
    alias = ('alias marvin="' + path + '/marvin_run.sh"')
    homefolder = os.path.expanduser('~')
    bashrc = os.path.abspath('%s/.bash_profile' % homefolder)
    with open(bashrc, 'r') as f:
        lines = f.readlines()
        if alias in lines:
            print('Please delete your alias command marvin in your .bashrc file')
            exit()
        else:
            out = open(bashrc, 'a')
            out.write(alias)
            out.close()
    os.system('source ' + bashrc)
    print('We need to install Homebrew so that we can install portaudio')
    os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    print('Installing portaudio')
    os.system('brew install portaudio')

elif check_os == 'Windows': pass
else:
    print ('We dont have a way to set up Marvin on your Operating System.\nIf this is a mistake make sure to report it as an issue at https://github.com/SavageCoder77/MARVIN_2.0')
print('\n\nAll files and installs completed\nYou can now run Marvin with the command marvin')
