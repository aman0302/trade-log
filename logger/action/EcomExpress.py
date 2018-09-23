import json

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
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'show-gt-md')))

        try:
            username_input = self.browser.find_element_by_name('username')
            password_input = self.browser.find_element_by_name('password')
        except:
            username_input = self.browser.find_elements_by_id('username')[0]
            password_input = self.browser.find_elements_by_id('password')[0]

        username_input.send_keys(self.credentials['ecom']['username'])
        password_input.send_keys(self.credentials['ecom']['password'])

        self.browser.find_element_by_css_selector("#log-form .btn1").click()

        self.on = True
        debugReport(":ECOM: Login successful")

    def upload(self):
        if self.on:
            try:
                WebDriverWait(self.browser, self.max_wait_for_load).until(
                    EC.presence_of_element_located((By.ID, 'soft')))
                self.browser.find_element_by_id("soft").click()

                WebDriverWait(self.browser, self.max_wait_for_load).until(
                    EC.presence_of_element_located((By.CLASS_NAME, 'headerText')))

                self.browser.find_element_by_name("file").send_keys(get_upload_excel_file_location())
                self.browser.find_element_by_css_selector(".col-md-6 button").click()

                WebDriverWait(self.browser, self.max_wait_for_load).until(
                    EC.presence_of_element_located((By.ID, 'md-title')))

                WebDriverWait(self.driver, 300)

            except Exception as e:
                errorReport(":ECOM: Upload failed because " + str(e))

            # debugReport(":ECOM: Upload complete")

    def login_and_upload(self):
        self.login()
        self.upload()
