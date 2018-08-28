#!/bin/bash
#File to install needed libraries into virtual env
source marvin-env/bin/activate
pip install pyttsx3
pip install -r requirements.txt
deactivate
