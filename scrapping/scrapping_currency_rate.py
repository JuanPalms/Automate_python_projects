"""
This python module implements an scrapper with beautiful soup in order
to get the exchange rate
"""
import requests
from bs4 import BeautifulSoup

def get_currency_rate(in_cur, out_cur):
    url=f'https://www.x-rates.com/calculator/?from={in_cur}&to={out_cur}&amount=1'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    rate = soup.find(id="content").find("div", class_="ccOutputBx").find("span",class_="ccOutputRslt")
    rate = rate.text
    rate = rate.split(" ")[0]
    print(rate)

get_currency_rate('USD','MXN')
