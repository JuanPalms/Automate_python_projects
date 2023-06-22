"""
This python module implements a call to the weather API, the API displays information about
an specified city in a span of time of 5 days every 3 hours
"""
import os
import sys
import requests
import pandas as pd

# Add the parent directory to sys.path
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from outils import load_config

config_f = load_config("config.yaml")


def create_weather_db(city, country_code):
    """
    This python module implements a process for building a weather database for the selected city
    Args:
    city(string): String that contains the name of the city you want the weather for
    country(strin): String that contains the code of the country in which the city is located
    Returns:
    weather_df(pandas dataframe): Pandas dataframe storing the weather conditions every 3 hours for the chosen city
    """
    r = requests.get(f'https://api.openweathermap.org/data/2.5/forecast?q={city},{country_code}&appid={config_f["api_key_weather"]}&units=metric')
    content = r.json()
    data=[]
    for element in content['list']:
        lista = []
        lista.append(city)
        lista.append(element['dt_txt'])
        lista.append(element['main']['temp'])
        lista.append(element['weather'][0]['description'])
        data.append(lista)
    weather_df=pd.DataFrame(data, columns=["City","Time","Temperature","Condition"])
    return weather_df

create_weather_db('Ciudad de Mexico', 'MEX').to_csv("weather_mx.csv")