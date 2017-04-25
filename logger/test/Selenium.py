from selenium import webdriver
from logger.utils.ExecutablePath import *

def get_browser():
    return webdriver.Chrome(executable_path=get_chromedriver_path())
