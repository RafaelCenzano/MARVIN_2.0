# Imports
from json import load # to open contacts.json to see contacts to be able to send email
from smtplib import SMTP # smtplib for connection and sending of email
from marvin.contacts import checkcontact
from email.mime.text import MIMEText # MIMEText for formatting
from email.mime.multipart import MIMEMultipart # MIMEMultipart changing sender


##########################
# File for sending email #
##########################

class Email:
    def __init__(self, contact_path, pass_path, email_recipient):
        self.email_recipient = email_recipient
        self.pass_path = pass_path
        self.contact_check = checkcontact(contact_path, email_recipient)
        with open(pass_path, 'r') as email_user_data: # open pass.json to get email password and username
            data = load(email_user_data) # load json
            self.email_user = data['email_address'] # get email address
            self.email_pass = data['email_password'] # get email password

    def email(self, subject, email_message):
        if self.contact_check != 'None':
            recipient_email = contact_data['contacts'][self.contact_check]['email'] # get email address of recipient

            # message area
            marvin_name = ('Marvin <' + self.email_user + '>')
            msg = MIMEMultipart() # formatting
            msg['From'] = marvin_name
            msg['To'] = recipient_email # input recipient email
            msg['Subject'] = subject # input subject
            msg.attach(MIMEText(email_message,'plain')) # add body
            text = msg.as_string() # format all text

            # sending code
            smtp_server = SMTP('smtp.gmail.com', 587) # connection to 587 port for gmail
            smtp_server.ehlo_or_helo_if_needed()
            smtp_server.starttls() #start connection
            smtp_server.ehlo_or_helo_if_needed()
            smtp_server.login(self.email_user, self.email_pass) # login with credentials
            smtp_server.sendmail(self.email_user, recipient_email, text) # send email
            smtp_server.quit() # quit connection
            print('Email Sent!') # done
        else: # recipient not in contacts
            speak('This user is not in our contacts use the "add contacts" command to add them') # user not found message