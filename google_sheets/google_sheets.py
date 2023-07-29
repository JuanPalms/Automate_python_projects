"""
This python module introduces the method to habdling google sheets.
"""
import pandas as pd
url1="https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2013"
url2="https://docs.google.com/spreadsheets/d/1D7U4A9c-hwWWYokmGWAQnUTKsyvEmV9syig8NJuVa84/gviz/tq?tqx=out:csv&sheet=2014"
data = pd.read_csv(url2)
print(data)