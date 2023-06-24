"""
This python module implements an scrapper with beautiful soup in order
to get the exchange rate
"""
import requests
from bs4 import BeautifulSoup
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('in_cur')
parser.add_argument('out_cur')

args = parser.parse_args()

def get_currency_rate(in_cur, out_cur):
    url=f'https://www.x-rates.com/calculator/?from={in_cur}&to={out_cur}&amount=1'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    rate = soup.find(id="content").find("div", class_="ccOutputBx").find("span",class_="ccOutputRslt")
    rate = rate.text
    rate = float(rate.split(" ")[0])
    return rate
    
current_rate = get_currency_rate(args.in_cur,args.out_cur)
print(current_rate)