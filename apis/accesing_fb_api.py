"""
This python module walks through a demonstration of accesing facebook api
"""
import requests
import json
from outils import load_config

config_keys = load_config("logging_key.yaml")

## Getting profile name
url = f"https://graph.facebook.com/v17.0/me?fields=id%2Cname&access_token={config_keys['access_token_fb']}"
response = requests.get(url)

## Getting the posts on my facebook

posts_url = f"https://graph.facebook.com/v17.0/3585553928357510?fields=id%2Cname%2Cposts&access_token={config_keys['access_token_fb']}"
posts_response = requests.get(posts_url)

## Getting one single post

image_url= f"https://graph.facebook.com/v17.0/3270879203158319?fields=link%2Cimages&access_token={config_keys['access_token_fb']}"

response = requests.get(image_url)
data = json.loads(response.text)
image=data["images"][0]["source"]

image_bytes = requests.get(image).content

with open('iumage.jpg','wb') as file:
    file.write(image_bytes)







