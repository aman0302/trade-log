import schedule, time

from logger.action.Persistance import persistance
from logger.action.Smallcase import smallcase
from logger.action.BrowserFactory import browser_factory

from logger.utils.Reporter import *


class smallcase_source():
    def __init__(self, config):
        self.begin = config['sm_begin']
        self.end = config['sm_end']
        self.interval = config['sm_interval']
        self.sheet_name = config['sm_sheet_name']
        self.pre_time = config['sm_pre_time']
        self.post_time = config['sm_post_time']
        self.on = False
        infoReport(":SMALLCASE SOURCE: initialized")

    def pre(self):
        debugReport(':SMALLCASE SOURCE: pre() called')
        self.browser = browser_factory().get_browser()
        self.smallcase = smallcase(self.browser)
        self.smallcase.login_if_not()
        self.on = True

    def process(self):
        debugReport(':SMALLCASE SOURCE: process() called')
        if not self.on:
            self.pre()
        try:
            smallcases = self.smallcase.fetch_record()
            persistance().persist_smallcase(smallcases, self.sheet_name)
        except:
            self.post()
            errorReport(':SMALLCASE SOURCE: process() failed')

    def post(self):
        debugReport(':SMALLCASE SOURCE: post() called')
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

        infoReport(':SMALLCASE SOURCE: smallcase scheduled')

        while True:
            schedule.run_pending()
            time.sleep(1)