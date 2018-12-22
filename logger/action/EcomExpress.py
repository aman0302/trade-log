import json, time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger.utils.ExecutablePath import *
from logger.utils.Reporter import *


class ecom:
    def __init__(self, browser):
        with open(get_credentials_path()) as data_file:
            self.credentials = json.load(data_file)
        self.browser = browser
        self.on = False
        self.max_wait_for_load = 5  # seconds

    def login(self):
        self.browser.get('https://cp.ecomexpress.in/#/login')
        WebDriverWait(self.browser, self.max_wait_for_load).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'pay_form')))

        time.sleep(3)

        username_input = self.browser.find_element_by_css_selector("input.logo")
        password_input = self.browser.find_element_by_css_selector(".password_contain input")

        username_input.send_keys(self.credentials['ecom']['username'])
        password_input.send_keys(self.credentials['ecom']['password'])

        self.browser.find_element_by_css_selector("input.button").click()

        time.sleep(3)

        self.on = True
        debugReport(":ECOM: Login successful")

    def upload(self):
        if self.on:

            # self.browser.find_element_by_css_selector(".close").click()
            # time.sleep(2)
            self.browser.find_elements_by_css_selector("a.ng-star-inserted")[6].click()
            # time.sleep(2)
            self.browser.find_elements_by_css_selector("a.ng-star-inserted")[7].click()
            time.sleep(2)
            self.browser.find_element_by_css_selector(".mat-select-placeholder").click()

            # self.browser.find_element_by_id("soft").click()

            try:
                if not self.is_reverse:
                    # WebDriverWait(self.browser, self.max_wait_for_load).until(
                    #     EC.presence_of_element_located((By.ID, 'soft')))
                    # self.browser.find_element_by_id("soft").click()
                    #
                    # WebDriverWait(self.browser, self.max_wait_for_load).until(
                    #     EC.presence_of_element_located((By.CLASS_NAME, 'headerText')))

                    self.browser.find_elements_by_css_selector(".mat-option-text")[0].click()
                else :
                    # WebDriverWait(self.browser, self.max_wait_for_load).until(
                    #     EC.presence_of_element_located((By.ID, 'reverse')))
                    # self.browser.find_element_by_id("reverse").click()
                    #
                    # WebDriverWait(self.browser, self.max_wait_for_load).until(
                    #     EC.presence_of_element_located((By.CLASS_NAME, 'headerText')))
                    self.browser.find_elements_by_css_selector(".mat-option-text")[1].click()

                time.sleep(2)
                self.browser.find_elements_by_css_selector(".mat-button-wrapper")[3].click()
                time.sleep(2)
                # self.browser.find_element_by_name("file").send_keys(self.path)
                self.browser.find_elements_by_id("file")[0].send_keys(self.path)
                self.browser.find_element_by_css_selector(".col-md-6 button").click()

                time.sleep(10)

                # WebDriverWait(self.browser, self.max_wait_for_load).until(
                #     EC.presence_of_element_located((By.CLASS_NAME, 'md-dialog-content')))

                # WebDriverWait(self.browser, 300)

            except Exception as e:
                errorReport(":ECOM: Upload failed because " + str(e))

    def login_and_upload(self, path, is_reverse):
        self.path = path
        self.is_reverse = is_reverse
        self.login()
        self.upload()
