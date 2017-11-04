from selenium import webdriver
from logger.utils.ExecutablePath import *


class browser_factory():

    def get_browser(self):
        #browser = webdriver.Chrome(executable_path=get_chromedriver_path())
        browser = webdriver.Firefox(executable_path=get_geckodriver_path())
        return browser
