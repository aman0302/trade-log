from selenium import webdriver
from logger.utils.ExecutablePath import *


class browser_factory():

    def get_browser(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.accept_untrusted_certs = True
        chrome_options.assume_untrusted_cert_issuer = True
        chrome_options.add_argument("--start-fullscreen")
        browser = webdriver.Chrome(executable_path=get_chromedriver_path(), chrome_options=chrome_options)

        # browser = webdriver.Firefox(executable_path=get_geckodriver_path())
        return browser
