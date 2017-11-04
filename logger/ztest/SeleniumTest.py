import sys, os
sys.path.append(os.path.dirname(os.getcwd()).replace('logger',''))
from logger.action.BrowserFactory import browser_factory

def test_selenium():
    browser = browser_factory().get_browser()
    browser.get("http://www.google.com")
    browser.quit()
