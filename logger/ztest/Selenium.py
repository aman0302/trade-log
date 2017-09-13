import unittest

from logger.action.BrowserFactory import browser_factory
from logger.action.Smallcase import smallcase


class selenium_test(unittest.TestCase):
    def test_login_to_kite(self):
        browser = browser_factory().get_browser()
        case = smallcase(browser)
        case.login_if_not()
        browser.close()


browser = browser_factory().get_browser()
browser.get("www.google.com")