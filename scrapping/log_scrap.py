"""
This python module automates the login and scrapping process for a demo page:
http://automated.pythonanywhere.com/login/ it stores the results in a txt file
"""
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
from outils import load_config
import schedule
from datetime import datetime

config_f = load_config('config.yaml')
url = "http://automated.pythonanywhere.com/login/"

def get_driver(url):
    """
    This function creates a driver to connect into a web page using chrome driver
    Args: 
    url (str) url containing url to parse
    Returns:
    driver
    """
    driver_folder=config_f['driver_folder']
    service = Service(os.path.join(driver_folder, "chromedriver"))
    # Set options to make browsing easier
    options = webdriver.ChromeOptions()
    #this blocks pop ups bars
    options.add_argument("disable-infobars")
    #make sure that the page starts maximized since some pages change content when minimized
    options.add_argument("start-maximized")
    # particular issues for linux computers
    options.add_argument("disable=dev-shm-usage")
    options.add_experimental_option("excludeSwitches",["enable-automation"])
    options.add_argument("disable-blink-features=AutomationControlled")
    options.add_argument("no-sandbox")
    driver = webdriver.Chrome(options=options,service=service)
    driver.get(url)
    return driver

def clean_text(element):
    numerical = float(element.split(": ")[1])
    return numerical

def main():
    """
    This function executes the main part of this module it signs in into the the
    web page by sending an username and password and thenb scrappes a dinamic value
    from the web page and stores it in a text file.
    """
    driver = get_driver(url)
    time.sleep(2)
    driver.find_element(by = "id",value = "id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by = "id",value = "id_password").send_keys("automatedautomated"+ Keys.RETURN)
    time.sleep(2)
    driver.find_element(by = "xpath", value = "/html/body/nav/div/a" ).click()
    time.sleep(2)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    # writting the scrapped text to a text file
    # If conditional checks for preexisting file otherwise creates the file for storing data
    if os.path.isfile('scrapped_time.txt')== True:
        with open('scrapped_time.txt', 'a') as appending_text_file:
            appending_text_file.write("\n")
            appending_text_file.write(str(clean_text(driver.find_element(by = "id", value = "displaytimer").text)))
            appending_text_file.write(',')
            appending_text_file.write(current_time)
            appending_text_file.close()
    else :
        with open('scrapped_time.txt', 'w') as creating_new_txt_file: 
            pass
        with open('scrapped_time.txt', 'a') as appending_text_file:
            appending_text_file.write("value,date")
            appending_text_file.write("\n")
            appending_text_file.write(str(clean_text(driver.find_element(by = "id", value = "displaytimer").text)))
            appending_text_file.write(',')
            appending_text_file.write(current_time)
            appending_text_file.close()   
        print("Scrapping file created successfully and added first scrapped element")
# initialize the main process every 10 seconds
schedule.every(10).seconds.do(main)
while True:
    schedule.run_pending()
    #after completition sleeps for 1 second
    time.sleep(1)




