"""
This python module gives an example of automated mail sending from an outlook mail
"""
import smtplib
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Add the parent directory to sys.path
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from outils import load_config

logging_keys = load_config('logging_key.yaml')

sender = os.getenv('outlook_email')
receiver = logging_keys['logging_mail']
password = os.getenv('outlook_password')

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message["Subject"] = "Hello, it's me"

body = """
<h1> Hello, its me...</h1>
I was wondering if after all these years you'd like to meet
To go over everything
They say that time's supposed to heal ya, but I ain't done much healing...
"""
#Declare in the mimetext object that its an html text
mimetext = MIMEText(body,'html')
# It expects a more specialized object
message.attach(mimetext)

server = smtplib.SMTP('smtp.office365.com',587)
server.starttls()
server.login(sender, password)
## need to convert the dictionary message to string
message_text = message.as_string()
server.sendmail(sender,receiver, message_text)
server.quit()