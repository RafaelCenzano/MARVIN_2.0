# Imports
import os
import platform

# Main Code
print ('Decting Operating System')
print ('Your os name is ' + os.name)
print ('Your os type is ' + platform.system())
print ('Your os version is ' + platform.release())

if platform.system() == 'Linux':
    print ('Linux')
elif platform.system() == 'Darwin':
    print ('Mac')
elif platform.system() == 'Windows':
    print ('Windows')
else:
    print ('We dont have a way to set up Marvin on your Operating System. \nIf this is a mistake make sure to report it as an issue at https://github.com/SavageCoder77/MARVIN_2.0')