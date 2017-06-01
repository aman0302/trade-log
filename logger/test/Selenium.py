from selenium import webdriver

from logger.action.Smallcase import Smallcase
from logger.utils.ExecutablePath import *

def get_browser():
    return webdriver.Chrome(executable_path=get_chromedriver_path())

def login_to_kite_test():
    browser = get_browser()
    smallcase = Smallcase(browser)
    smallcase.login_if_not()
    browser.close()