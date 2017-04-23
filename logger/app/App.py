import schedule
import time

from selenium import webdriver

from logger.action.Kite import Kite
from logger.action.Smallcase import Smallcase
from logger.action.GoogleSheet import GoogleSheet
from logger.utils.ExecutablePath import *
from logger.utils.Time import *


class App:
    def __init__(self):
        logging.basicConfig(filename=get_log_file_name(), level=logging.INFO)
        logging.info('################SERVER STARTED###############')

        # self.browser = webdriver.Firefox(executable_path=executablepath.get_geckodriver_path())
        self.browser = webdriver.Chrome(executable_path=get_chromedriver_path())
        self.login_prerequisite()


    def login_prerequisite(self):
        try:
            self.smallcase = Smallcase(self.browser)
            self.smallcase.login_if_not()

            self.googlesheet = GoogleSheet()

        except:
            self.browser.quit()

    def execute(self):
        smallcases = self.smallcase.fetch_record()
        self.googlesheet.insert_data(smallcases)
        # return schedule.CancelJob

    def start(self):

        start = 330 # 0900 - 0530 = 0330
        end = 1000 # 1530 - 0530 = 1000

        increment = 1

        while start < (end + increment):
            t = military_time_to_string(start)

            logging.info('Scheduled for : %s', t)
            print('Scheduled for : ', t)

            schedule.every().monday.at(t).do(self.execute)
            schedule.every().tuesday.at(t).do(self.execute)
            schedule.every().wednesday.at(t).do(self.execute)
            schedule.every().thursday.at(t).do(self.execute)
            schedule.every().friday.at(t).do(self.execute)
            # schedule.every().saturday.at(t).do(self.execute)
            # schedule.every().sunday.at(t).do(self.execute)

            start = mililary_time_adjust_rolling_window(start + increment)

        while True:
            schedule.run_pending()
            time.sleep(1)