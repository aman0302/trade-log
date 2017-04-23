import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logger.models.SmallcaseModel import SmallcaseModel
from logger.action.Kite import Kite
from logger.utils.Time import *


class Smallcase:
    def __init__(self, browser):
        self.browser = browser
        self.kite = Kite(self.browser)

    def is_logged_in(self):
        self.browser.get('https://www.smallcase.com/investments/current')
        if 'login' in self.browser.current_url:
            return False
        else:
            return True

    def login_if_not(self):
        if not self.is_logged_in():
            print('SMALLCASE not logged in. Logging in ...')
            logging.info('SMALLCASE not logged in. Logging in ...')
            self.login()

        else:
            print('SMALLCASE already logged in.')
            logging.info('SMALLCASE already logged in.')

    def login(self):
        self.kite.login_if_not()
        if not self.is_logged_in():
            kitelogin = self.browser.find_element_by_class_name('kite-login')
            kitelogin.click()
            WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'username')))

    def fetch_record(self):
        self.login_if_not()

        self.browser.get('https://www.smallcase.com/investments/current')
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'marker-manage')))

        smallcases_meta = self.browser.find_elements_by_class_name('metadata')
        smallcases_stats = self.browser.find_elements_by_class_name('stats')

        smallcases = []

        timestamp = get_current_timestamp()

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

            sm = SmallcaseModel(name=name, index=index, value=value, investment=investment, pnl=pnl,
                                actual_pnl=actual_pnl, bought_on=bought_on, timestamp=timestamp)

            smallcases.append(sm)

        print(timestamp, ' : Fetched smallcases')
        logging.info('%s : Fetched smallcases', timestamp)
        return smallcases
