"""
This python module gives an example of automated mail sending from an outlook mail
"""
import smtplib
import os
import sys

# Add the parent directory to sys.path
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from outils import load_config

logging_keys = load_config('logging_key.yaml')

### when sending an outlook automated mail it works fine with a regular logging password
## The passwords and emails passed in this code line are stored in the env file of the computer
## visit: https://pythonhow.com/how/store-python-passwords-securely-on-windows-mac-and-linux/
### to learn about securely storing passwords in your computer
sender = os.getenv('outlook_email')
receiver = logging_keys['logging_mail']
password = os.getenv('outlook_password')

message = """\
Subject: Hello, its me..


I was wondering if after all these years you'd like to meet
To go over everything
They say that time's supposed to heal ya, but I ain't done much healing... 
"""

server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender, password)
server.sendmail(sender,receiver, message)
server.quit()

