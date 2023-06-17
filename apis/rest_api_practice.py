"""
This python module implements userfriendly call to News api
"""
import requests
from outils import load_config

config_f = load_config("config.yaml")

r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2023-05-18&to=2023-05-25&sortBy=popularity&language=en&apiKey=232083e9c72441509c717046236f8a6b')
content = r.json()

articles = content['articles']

def get_news(topic,start_day,end_day, start_month, end_month, start_year='2023', end_year='2023', languague='en', api_key=config_f['api_key']):
    url = f'https://newsapi.org/v2/everything?qInTitle={topic}%20market&from={start_year}-{start_month}-{start_day}&to={end_year}-{end_month}-{end_day}&sortBy=popularity&language={languague}&apiKey={api_key}'
    r = requests.get(url)
    content= r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE\n'{article['title']},'\nDESCRIPTION\n',{article['description']}")
    return results

print(get_news(topic='space', start_day='18',end_day='25', start_month='05', end_month='05'))