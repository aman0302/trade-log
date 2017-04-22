from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from logger.models.SmallcaseModel import smallcase_model


class smallcase:
    def __init__(self, browser):

        self.browser = browser

    def login_if_not(self):

        self.browser.get('https://www.smallcase.com/investments/current')
        if 'login' in self.browser.current_url:
            self.login()

    def login(self):

        kitelogin = self.browser.find_element_by_class_name('kite-login')
        kitelogin.click()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'username')))

    def fetch_record(self):

        self.browser.get('https://www.smallcase.com/investments/current')

        smallcases_meta = self.browser.find_elements_by_class_name('metadata')
        smallcases_stats = self.browser.find_elements_by_class_name('stats')

        print(len(smallcases_meta))
        print(len(smallcases_stats))

        for i, smallcase_stat in enumerate(smallcases_stats):

            smallcase_meta = smallcases_meta[i].text.splitlines()
            name = smallcase_meta[0]
            bought_on = smallcase_meta[1].replace('Bought on', '').replace('· See orders', '').trim()

            lines = smallcase_stat.text.splitlines()

            index = lines[1]
            value = lines[3]
            investment = lines[5]
            pnl = lines[6].replace('Current P&L').trim()
            actual_pnl = lines[7]

            sm = smallcase_model(name=name, index=index, value=value, investment=investment, pnl=pnl,
                                 actual_pnl=actual_pnl, bought_on=bought_on)

            print(sm)