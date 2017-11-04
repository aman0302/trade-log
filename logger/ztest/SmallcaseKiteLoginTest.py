import sys, os, unittest
sys.path.append(os.path.dirname(os.getcwd()).replace('logger',''))
from logger.action.BrowserFactory import browser_factory
from logger.action.Smallcase import smallcase
from logger.action.Kite import kite

class LoginTest(unittest.TestCase):
    def test_smallcase_login(self):
        browser = browser_factory().get_browser()
        s=smallcase(browser)
        s.login_if_not()
        browser.quit()

    def test_kite_login(self):
        browser = browser_factory().get_browser()
        k = kite(browser)
        k.login_if_not()
        browser.quit()