"""
This python module implements and automated dowloading of the data of Yahoo Finance of custom periods and compnies choosen by the user
"""
import requests
from datetime import datetime
import time

ticker = input("Enter the stock symbol:")
from_date = input('Enter start date in yyyy/mm/dd format:')
to_date = input('Enter end date in yyyy/mm/dd format:')

from_datetime=datetime.strptime(from_date,'%Y/%m/%d')
to_datetime=datetime.strptime(to_date,'%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


historical_stocks = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1d&events=history&includeAdjustedClose=true'
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}
content = requests.get(historical_stocks, headers=headers).content

# Change date format for filename to use hyphens instead of slashes
from_date_filename = from_date.replace("/", "-")
to_date_filename = to_date.replace("/", "-")

# Use the new date formats in the filename
with open(f'data_{ticker}_{from_date_filename}_{to_date_filename}.csv','wb') as file:
    file.write(content)