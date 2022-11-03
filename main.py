"""
Author: Sharon Steinke

Sends an email script to the address located in the .cvs document.

Reflection:
This was a fun program to write. Gmail has very strict accessabilty and security measures
which made what seemed an easy problem in to a more complex problem.
To solve you have to approve the "main.py" app in your gmail account
and use the password Gmail gives you instead of your normal login password. 

TO USE:
If you have gmail:
Before you can even run this program, you have to get this app approved by your gmail
account.

1. Update client information in "client.csv". You must download it as a CSV
(comma separated value) from google drive. Rename and override old "client.csv"
with new one.

2. Double check that all e-mails are in appropriate cell, there is only one e-mail listed per client,
and e-mail is formatted correctly.

3. Save a copy of old "script.txt" to email-history with a new name
(whatever helps you keep organized).

4. Write new e-mail in "script.txt". Formatted like "the example_script.txt"
Make sure to save it.

5. Update subject line, login email and password, and sender email, in the code below look for the comments directing you 
where to edit the code. 


"""
import csv
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import smtplib
import os

def get_clients(csvfile):
    """
    reads cvs file
    """
    email_list = []
    with open(csvfile, newline='', encoding="utf8") as fin:
        reader = csv.DictReader(fin)
        for row in reader:
            email_list.append((row['First Name'], row['Last Name'], row['E-mails']))
    return email_list

def draft_email(first_name='jane', last_name='doe'):
    """drafts email"""
    with open('script.txt', encoding='utf8') as fin:
        lines = fin.readlines()
        lines[0]=(f'{lines[0].strip()} {first_name} {last_name},\n')
        draft = ''.join(lines)
        return draft

def main():
    """
    runs the main program
    """
#FIX::ME NEED TO ADD A TRY EXCEPT FOR INVALID/NO EMAIL
    clients = get_clients("clients.csv")

    for client in clients:
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.ehlo()
        session.starttls()
#CHANGE USER LOGIN AND PASSWORD BELOW:
        session.login("", "")

        message = MIMEMultipart()
# CHANGE SUBJECT BELOW:
        message["Subject"] = ""
        body = draft_email(client[0], client[1])
        message.attach(MIMEText(body))

        logo = open("logo.png", 'rb').read()
        message.attach(MIMEImage(logo, name=os.path.basename("logo.png")))
#CHANGE SENDER EMAIL BELOW:
        session.sendmail(from_addr="",
        to_addrs=str(client[2]), msg = message.as_string())

    session.quit()


if __name__ == '__main__':
    main()
