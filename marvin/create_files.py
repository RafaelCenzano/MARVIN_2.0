import marvin.webscrape
from platform import system, release
import json
import os
contacts_path = os.path.join('marvin','json','contacts.json')

check_os = system()
os_release = release()
marvin_version = webscrape.getVersion()
try:
    with open('Os.json', 'w') as outfile:
        var2 = {"Marvin_Release":marvin_version,"Os_data":{"OS":check_os,"os_release":os_release},"apps":{"IOS":"INACTIVE"},"voice":"female"}
        json.dump(var2, outfile)
    with open(contacts_path, 'w') as outfile1:
        var = {"contacts":{},"nicks":{}}
        json.dump(var, outfile1)
except Exception as e:
    print('We ran into a problem\nPlease report this issue ' + str(e) + '\nFiles couldn\'t be created properly')