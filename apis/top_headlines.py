"""
This python module implements the extraction of News headlines from News api
"""
import requests
from outils import load_config

config_f = load_config("config.yaml")


def get_news(country, api_key=config_f['api_key']):
    url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}'
    r = requests.get(url)
    content= r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{article['title']},'\nDESCRIPTION\n',{article['description']}")
    return results

print(get_news(country='us'))