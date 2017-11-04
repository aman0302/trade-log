import schedule, time, logging


from logger.action.Persistance import persistance
from logger.action.Smallcase import smallcase
from logger.action.BrowserFactory import browser_factory

from logger.utils.Time import *


class smallcase_source():
    def __init__(self):
        self.begin = 1500
        self.end = 1600
        self.interval = 1
        self.sheet_name = "trade-log1"
        self.pre_time = 825
        self.post_time = 1600
        self.on = False

    def pre(self):
        self.browser = browser_factory().get_browser()
        self.smallcase = smallcase(self.browser)
        self.smallcase.login_if_not()
        self.on = True

    def process(self):

        if not self.on:
            self.pre()
        try:
            smallcases = self.smallcase.fetch_record()
            persistance().persist_smallcase(smallcases, self.sheet_name)
        except:
            self.post()
            print(':: SMALLCASE SOURCE:: process() failed ...')
            logging.info(':: SMALLCASE SOURCE:: process() failed ...')


    def post(self):
        if self.on:
            self.browser.quit()
            self.browser = None
            self.on = False

    def start(self):
        schedule.every().monday.at(military_time_to_string(self.pre_time)).do(self.pre)
        schedule.every().tuesday.at(military_time_to_string(self.pre_time)).do(self.pre)
        schedule.every().wednesday.at(military_time_to_string(self.pre_time)).do(self.pre)
        schedule.every().thursday.at(military_time_to_string(self.pre_time)).do(self.pre)
        schedule.every().friday.at(military_time_to_string(self.pre_time)).do(self.pre)

        while self.begin < (self.end + self.interval):
            military_time = military_time_to_string(self.begin)

            schedule.every().monday.at(military_time).do(self.process)
            schedule.every().tuesday.at(military_time).do(self.process)
            schedule.every().wednesday.at(military_time).do(self.process)
            schedule.every().thursday.at(military_time).do(self.process)
            schedule.every().friday.at(military_time).do(self.process)

            self.begin = mililary_time_adjust_rolling_window(self.begin + self.interval)

        schedule.every().monday.at(military_time_to_string(self.post_time)).do(self.post)
        schedule.every().tuesday.at(military_time_to_string(self.post_time)).do(self.post)
        schedule.every().wednesday.at(military_time_to_string(self.post_time)).do(self.post)
        schedule.every().thursday.at(military_time_to_string(self.post_time)).do(self.post)
        schedule.every().friday.at(military_time_to_string(self.post_time)).do(self.post)

        while True:
            schedule.run_pending()
            time.sleep(1)
