import gspread
import logging

from oauth2client.service_account import ServiceAccountCredentials

from logger.utils.ExecutablePath import *

class GoogleSheet:

    def __init__(self):
        scope = "https://www.googleapis.com/auth/drive"
        credentials = ServiceAccountCredentials.from_json_keyfile_name(get_google_drive_secret_path(), scope)

        self.gs = gspread.authorize(credentials)
        self.open_sheet()

    def open_sheet(self):
        self.sheet = self.gs.open("trade-log")
        logging.info('Opened sheet.')

    def insert_data(self, smallcases):
        for smallcase in smallcases:
            try:
                curr_worksheet = self.sheet.worksheet(smallcase.name)
            except:
                logging.info('Creating worksheet for ',smallcase.name)
                curr_worksheet = self.sheet.add_worksheet(title=smallcase.name, rows=2, cols=5)

            curr_worksheet = self.sheet.worksheet(smallcase.name)

            curr_worksheet.append_row(smallcase.get_ordered_data())