"""
This python module automates the process of sending emails to multiple receivers
"""

import os
import sys
import yagmail

# Add the parent directory to sys.path
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from outils import load_config


loggin_keys = load_config('logging_key.yaml')

sender = 'palmeros.scrapp@gmail.com'

receiver = 'juanfrancisco.palmeros@outlook.com'

subject = "First email automated"

content = """
Here is the content of the first email we are sending
Hi!
"""

yag = yagmail.SMTP(user= sender, password=loggin_keys['app_password_mail'])
for receiver in loggin_keys['receivers_list']:
    yag.send(to=receiver, subject=subject, contents=content)