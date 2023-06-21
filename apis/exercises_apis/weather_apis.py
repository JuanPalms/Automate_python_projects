"""
This python module implements a call to the weather API, the API displays information about
an specified city in a span of time of 5 days every 3 hours
"""
import os
import sys
import requests

# Add the parent directory to sys.path
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from outils import load_config

config_f = load_config("config.yaml")

r = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q=München,DE&appid={config_f["api_key_weather"]}&units=metric')
content = r.json()

print(content[0])
