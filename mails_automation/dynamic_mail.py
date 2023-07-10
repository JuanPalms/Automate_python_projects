"""
This python module automates the process of sending emails to multiple receivers
and creation of file specific attachments for each receiver
"""
import os
import sys
import yagmail
import pandas as pd

# Add the parent directory to sys.path
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from outils import load_config

# Load logging credentials (sender email)
loggin_keys = load_config('logging_key.yaml')
sender = loggin_keys['logging_mail']

yag = yagmail.SMTP(user= sender, password=loggin_keys['app_password_mail'])

data = pd.read_csv('contacts.csv')

def generate_file(filename, content):
    """
    This functions generates a simple file
    based on the given name and the content
    """
    with open(f'{filename}.txt', 'w') as file:
        file.write(str(content))

for index, row in data.iterrows():
    name = row['name']
    amount = row['amount']
    receiver_email = row['email']
    
    generate_file(name,amount)

    subject = "This is the subject!"
    content = [f"""Dear {name}: \n
    We send this email to inform you that you have a pending payment in your credit car for the amout of: \n
    {amount} MXN. That you have to pay before next week. 
    We attached the bill with the amount details,
    Regards!
    """,
    name]

    yag.send(to =receiver_email, subject=subject, contents= content)
    print('Email sent!')
