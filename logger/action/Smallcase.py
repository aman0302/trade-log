from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logger.models.SmallcaseModel import smallcase_model
from logger.action.Kite import kite
from logger.utils.Reporter import *


class smallcase:
    def __init__(self, browser):
        self.browser = browser
        self.kite = kite(browser)

    def is_logged_in(self):
        self.browser.get('https://www.smallcase.com/investments/current')
        if 'login' in self.browser.current_url:
            return False
        else:
            return True

    def login_if_not(self):
        if not self.is_logged_in():
            infoReport(':SMALLCASE: not logged in. Logging in ...')
            self.login()

        else:
            infoReport(':SMALLCASE: already logged in.')

    def login(self):
        self.kite.login_if_not()
        if not self.is_logged_in():
            kitelogin = self.browser.find_element_by_class_name('kite-login')
            kitelogin.click()
            WebDriverWait(self.browser, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'smallcases')))

    def fetch_record(self):
        self.login_if_not()
        self.browser.get('https://www.smallcase.com/investments/current')
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'marker-manage')))

        timestamp = get_current_timestamp()
        smallcases_meta = self.browser.find_elements_by_class_name('metadata')
        smallcases_stats = self.browser.find_elements_by_class_name('stats')
        smallcases = []

        for i, smallcase_stat in enumerate(smallcases_stats):
            smallcase_meta = smallcases_meta[i].text.splitlines()
            name = smallcase_meta[0]
            bought_on = smallcase_meta[1].replace('Bought on', '').replace('· See orders', '').strip()

            lines = smallcase_stat.text.splitlines()

            index = lines[1]
            value = lines[3]
            investment = lines[5]
            pnl = lines[6].replace('Current P&L', '').strip()
            actual_pnl = lines[7]

            sm = smallcase_model(name=name, index=index,
                                 value=value, investment=investment,
                                 pnl=pnl, actual_pnl=actual_pnl,
                                 bought_on=bought_on, timestamp=timestamp)

            smallcases.append(sm)

        debugReport(':SMALLCASE: Fetched smallcases')
        return smallcases
