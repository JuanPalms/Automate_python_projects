"""
This python module implements the extraction of the information available at https://titan22.com/
in particular it extract the model, brand, color and price of the footwear in the page
"""
import os
import sys
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pandas as pd


# Add the parent directory to sys.path
current_dir = os.getcwd()
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from outils import load_config, get_driver, load_keys

# charge the keys to logg you must replace the keys with your own
keys_f = load_keys('logging_key.yaml')

path_retailer='https://titan22.com/account/login?return_url=%2Faccount'

def logging(url):
    """
    This module implements the logging and scrapping process of a reatual page 
    Args:
    url (string): url to login
    """
    tenis=[]
    tenis_pd=pd.DataFrame()
    driver=get_driver(url)
    time.sleep(3)
    driver.find_element(by = "xpath",value = "/html/body/main/article/section/div/div[1]/form/div[1]/input").send_keys(keys_f["logging_mail"])
    time.sleep(3)
    driver.find_element(by = "xpath",value = "/html/body/main/article/section/div/div[1]/form/div[2]/input").send_keys(keys_f["logging_key"]+ Keys.RETURN)
    time.sleep(4)
    driver.find_element(by = "xpath", value = "/html/body/header/div[1]/div[1]/div/div[2]/nav[1]/ul/li[2]/a" ).click()
    time.sleep(4)
    try:
        for numero in range(1,100):
            numero = "/html/body/main/article/div/div/div/div[1]/section/div[3]/div[{}]/div/a".format(numero)
            element= driver.find_element(by = "xpath", value = numero).text.split("\n")
            tenis.append(element)    
    except:
        for pagina in range(0,20):
            try: 
                driver.find_element(By.LINK_TEXT, 'Next »').click()
                time.sleep(3)
                for numero in range(1,16):
                    numero = "/html/body/main/article/div/div/div/div[1]/section/div[3]/div[{}]/div/a".format(numero)
                    element= driver.find_element(by = "xpath", value = numero).text.split("\n")
                    tenis.append(element)   
            except:
                print(f"web scrapping stopped at {len(tenis)} element")
    return tenis

tennis=logging(path_retailer)
df_tennis = pd.DataFrame(tennis, columns=['Marca', 'Modelo', 'Precio original','Precio descuento'])

df_tennis = (
    df_tennis
    # Extraer el numero de episodio
    .assign(
        nombre_producto = lambda df_: df_['Modelo'].str.split("'").str[0].str.strip(),
        estilo = lambda df_: df_['Modelo'].str.split("'").str[1].str.strip(),
        precio_original = lambda df_: (df_['Precio original'].str.replace('₱', '', regex=True)
                                       .str.replace('.00', '', regex=False)
                                       .str.replace(',', '', regex=False)),
        precio_descuento = lambda df_: (df_['Precio descuento'].str.replace('₱', '', regex=True)
                                       .str.replace('.00', '', regex=False)
                                       .str.replace(',', '', regex=False))
    )
    .drop(columns=['Modelo','Precio original','Precio descuento'])
)

df_tennis.to_csv('tennis_prices.csv')