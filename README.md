# MARVIN_2.0
![alt text](https://img.shields.io/github/license/SavageCoder77/MARVIN_2.0.svg)
![alt text](https://img.shields.io/github/stars/SavageCoder77/MARVIN_2.0.svg)
![alt text](https://img.shields.io/github/forks/SavageCoder77/MARVIN_2.0.svg)
![alt text](https://img.shields.io/github/issues/SavageCoder77/MARVIN_2.0.svg)
![alt text](https://img.shields.io/badge/Marvin%20Version-0.0.3-brightgreen.svg)

## Table of Contents
1. [Description](#description)
2. [Installation](#installation)
3. [Usage](#usage)
4. [License](#license)
5. [Commands](#commands)

## Description
Marvin2.0 is a python program that can open websites and do simple webscrape tasks. Full command list at the bottom of the README.

## Installation
This project uses has a setup.py that should work on MAC, Windows, and most Linux distributions:
```
git clone https://github.com/SavageCoder77/MARVIN_2.0.git
python2.7 setup.py
```

## Usage
To start Marvin you run:
```
python2.7 Marvin_Script.py
```
From there you login with a User. If its your first time running Marvin you have to login with ADMIN to create a new User to login and use Marvin's [commands](#commands). After you login you read the instructions on screen and you should be able to run any [commands](#commands).

## License
This project is licensed under the terms of the MIT license. See the LICENSE file.

## Commands
Full list of all commands and description of what the command does


open reddit {subreddit} _|_ will open the subreddit that you input


rotten tomatoes {movie} _|_ will tell you the rotten tomatoes raiting, IMDb raiting, and audience score of the movie you input


google search {search}  _|_ will open the google search of your search


where is {location} _|_ will open your location in google maps


youtube {video name} _|_ will open the first video that shows up for your video name


amazon {amazon search}  _|_ will open amazon's search of you input


time in {location} _|_ will open the time in your location on time.is


contact list {alias = contacts} _|_  will show you contacts  


add contact {alias = new contact} _|_ will allow you to create any contact  


remove contact {alias = delete contact} _|_ will allow you to remove any contact you have


send email _|_ will allow you to send an email as long as you input correct credentials during setup.py. Use ADMIN to correct or add email credentials


open calculator {alias = run calculator} _|_ opens a GUI calculator in a parralel thread allowing for commands at the same time


standby _|_ stops input of commands


logout {alias = relog} _|_ allows you to log in with a different User


exit {alias = quit} _|_ exits the program
