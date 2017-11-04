import gspread
from oauth2client.service_account import ServiceAccountCredentials
from logger.utils.ExecutablePath import *
from logger.utils.Reporter import *


class googlesheet:
    def __init__(self, sheet_name):

        self.sheet_name = sheet_name
        self.scope = "https://www.googleapis.com/auth/drive"
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(get_google_drive_secret_path(), self.scope)

        self.gs = gspread.authorize(self.credentials)
        self.open_sheet()

    def open_sheet(self):
        self.sheet = self.gs.open(str(self.sheet_name))
        debugReport(':GOOGLESHEET: Opened sheet.')

    def insert_smallcase_data(self, smallcases):
        for smallcase in smallcases:
            try:
                self.insert(smallcase)
            except:
                errorReport(':GOOGLESHEET: Failed. Retrying again.' + smallcase.name)
                self.__init__()
                self.insert(smallcase)

    def insert(self, smallcase):
        try:
            curr_worksheet = self.sheet.worksheet(smallcase.name)
        except:
            infoReport(':GOOGLESHEET: Sheet does not exist. Creating worksheet for ' + smallcase.name)
            curr_worksheet = self.sheet.add_worksheet(title=smallcase.name, rows=2, cols=5)

        try:
            curr_worksheet = self.sheet.worksheet(smallcase.name)
            curr_worksheet.append_row(smallcase.get_ordered_data())
        except:
            errorReport(':GOOGLESHEET: Failed while puttind data for' + smallcase.name)

        debugReport(':GOOGLESHEET:' + smallcase.name)

        return True
