"""
Author: Sharon Steinke

Sends an email script to the address located in the .cvs document.

Reflection:
All in all a fun project that my friend who owns small business asked me to write for her company
I would not reccommend trying to get gmail to work. I did, eventually, but I wouldn't
do it again.
"""
import csv
import smtplib

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
    password = ''
    email = ''
    clients = get_clients("clients.csv")

    for client in clients:
        session = smtplib.SMTP('smtp.gmail.com', 587)

        session.starttls()

        session.login(email, password)

        message = draft_email(client[0], client[1])

        session.sendmail(email, str(client[2]), message)

    session.quit()


if __name__ == '__main__':
    main()
