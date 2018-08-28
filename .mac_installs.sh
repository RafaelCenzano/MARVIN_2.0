#!/bin/bash
#File to install needed libraries into virtual env
source marvin-env/bin/activate
pip install --editable git+https://github.com/nateshmbhat/pyttsx3.git@master#egg=pyttsx3
pip install -r requirements.txt
deactivate
