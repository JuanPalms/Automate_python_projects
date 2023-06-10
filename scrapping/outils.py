import os
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

CURRENT = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(CURRENT)

# Function to load yaml configuration file
def load_config(config_name):
    """
    Sets the configuration file path
    Args:
    config_name: Name of the configuration file in the directory
    Returns:
    Configuration file
    """
    with open(os.path.join(ROOT, config_name), encoding="utf-8") as conf:
        config = yaml.safe_load(conf)
    return config

def load_keys(keys_file):
    """
    Sets the keys file path
    Args:
    config_name: Name of the keys file in the directory
    Returns:
    Keys file
    """
    with open(os.path.join(ROOT, keys_file), encoding="utf-8") as keys:
        keys = yaml.safe_load(keys)
    return keys


def get_driver(url):
    """
    This function creates a driver to connect into a web page using chrome driver
    Args: 
    url (str) url containing url to parse
    Returns:
    driver
    """
    config_f = load_config('config.yaml')
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