# Imports
import os
from platform import system, release
from json import dump, load
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
def unix_linux(pass_path):
    os.system('pip install virtualenv==16.0.0')
    os.system('virtualenv --python=/usr/bin/python2.7 marvin-env')
    os.system('chmod 755 .installs.sh')
    os.system('./.installs.sh')
    env = ('source ' + path + '/marvin-env/bin/activate')
    script = (path + '/marvin-env/bin/python2.7 ' + path + '/Marvin_Script.py')
    cd = ('cd ' + path)
    script2 = (path + '/marvin-env/bin/python2.7 ' + path + '/marvin/rest-server/rest-server.py')
    cd2 = ('cd ' + path + '/marvin/rest-server')
    # marvin script start file
    out2 = open('marvin_run.sh', 'a')
    out2.write('#!/bin/bash')
    out2.write('\n')
    out2.write(env)
    out2.write('\n')
    out2.write(cd)
    out2.write('\n')
    out2.write(script)
    out2.write('\n')
    out2.write('deactivate')
    out2.close()
    # rest server start file
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
    os.system('chmod 755 marvin/rest-server/start_rest.sh')
    os.system('chmod 755 marvin_run.sh')
    os.system('chmod 755 setup.sh')
    os.system('./setup.sh')
    with open(pass_path, 'w') as outfile2:
        var1 = {"email_address":email_usr, "email_password":email_pass, "logins":{"ADMIN":{"pass":pass_new}}}
        dump(var1, outfile2)
    print('\n\nAll files and installs completed\nYou can now run Marvin with the command marvin')

check_os = system()
os_release = release()
print ('Decting Operating System')
print ('Your os type is ' + check_os)
print ('Your os version is ' + os_release)

print('Creating needed files')

pass_path = os.path.join('marvin','json','pass.json')

print('We need your email to be able to send emails')
print('\n#####\nYou will need to change an email setting that allows less secure apps\n#####\n')
print('\nIf you dont want the email function type none')
print('Please type email address')
email_usr = raw_input('>')
print('Please type email password')
email_pass = raw_input('>')

print('Starting installs')

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
    unix_linux(pass_path)

elif check_os == 'Darwin':
    alias = ('alias marvin="' + path + '/marvin_run.sh"')
    homefolder = os.path.expanduser('~')
    bashrc = os.path.abspath('%s/.bash_profile' % homefolder)
    with open(bashrc, 'r') as f:
        lines = f.readlines()
        if alias in lines:
            print('Please delete your alias command marvin in your ~/.bash_profile file')
        else:
            out = open(bashrc, 'a')
            out.write(alias)
            out.close()
            os.system('source ' + bashrc)
    print('We need to install Homebrew so that we can install portaudio')
    os.system('/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"')
    print('Installing portaudio')
    os.system('brew install portaudio')
    unix_linux(pass_path)

elif check_os == 'Windows':
    python_path = os.path.join('C:','\\Python27','python.exe')
    if os.path.isfile(python_path) == False:
        print("Python2.7 not installed or is not in the default location. Please input your path to python.exe in your Python27 folder. \nExample:\nC:\\Documents\\Programming\\Python27\\python.exe\n\nIf you do not have python installed please close the program and install it here: https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi and install it in the default location")
        python_path = raw_input('>')
        if os.path.isfile(python_path) == False:
            print('Please install python2.7 here: https://www.python.org/ftp/python/2.7.15/python-2.7.15.msi')
            exit()
    python_path_list = python_path.split("\\")
    python_path_list.remove('python.exe')
    fixed_python_path = ("\\").join(python_path_list)
    pip_path = (fixed_python_path + '\\Scripts\\pip.exe')
    if os.path.isfile(pip_path) == False:
        print('You need to install pip. \nDownload the pip install file here: https://bootstrap.pypa.io/get-pip.py and run it with python')
        exit()
    os.system(pip_path + ' install -r requirements.txt')
    with open(pass_path, 'w') as outfile2:
        var1 = {"email_address":email_usr, "email_password":email_pass, "logins":{"ADMIN":{"pass":pass_new}}}
        dump(var1, outfile2)
    os.system(path + '\\marvin-env\\Scripts\\python.exe marvin\\create_files.py')
    with open('Os.json', 'r') as os_data:
        os_data_loaded = load(os_data)
    with open('Os.json', 'w') as outfile:
        os_data_loaded = {"python_path":python_path}
        dump(os_data_loaded, outfile)
    out = open('marvin.bat', 'w')
    out.write('@echo off\n')
    out.write(python_path + ' ' + path + '\\Marvin_Script.py')
    out.close()
    print('\n\nAll files and installs completed\nYou can now run Marvin by typing marvin in this folder or add this ' + path + ' to a new line in your path enviorment variable')
else:
    print ('We dont have a way to set up Marvin on your Operating System.\nIf this is a mistake make sure to report it as an issue at https://github.com/SavageCoder77/MARVIN_2.0')