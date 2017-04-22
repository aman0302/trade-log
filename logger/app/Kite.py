from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
from logger.app.ExecutablePath import *


class kite:
    def __init__(self, browser):
        with open(get_credential_json_path()) as data_file:
            self.credentials = json.load(data_file)
            self.questions = self.credentials['questions']
            self.answers = self.credentials['answers']
        self.browser = browser


    def login_if_not(self):
        self.browser.get('https://kite.zerodha.com/dashboard/?login=true')

        url = self.browser.current_url
        if '#loggedout' in url:
            return self.login()

    def login(self):
        username_input = self.browser.find_element_by_name('user_id')
        password_input = self.browser.find_element_by_name('password')

        username_input.send_keys(self.credentials['username'])
        password_input.send_keys(self.credentials['password'])

        self.browser.find_element_by_name('login').click()

        self.answer_security_questions()

    def answer_security_questions(self):
        first_que = self.browser.find_element_by_class_name('first').text
        second_que = self.browser.find_element_by_class_name('second').text

        first_ans = self.answers[self.questions.index(first_que)]
        second_ans = self.answers[self.questions.index(second_que)]

        first_que_input = self.browser.find_element_by_name('answer1')
        second_que_input = self.browser.find_element_by_name('answer2')

        first_que_input.send_keys(first_ans)
        second_que_input.send_keys(second_ans)

        self.browser.find_element_by_name('twofa').click()

        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'user-id')))
