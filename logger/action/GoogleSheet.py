import gspread

from oauth2client.service_account import ServiceAccountCredentials

from logger.utils.ExecutablePath import *


class GoogleSheet:
    def __init__(self):
        self.scope = "https://www.googleapis.com/auth/drive"
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(get_google_drive_secret_path(), self.scope)

        self.gs = gspread.authorize(self.credentials)
        self.open_sheet()


    def open_sheet(self):
        self.sheet = self.gs.open("trade-log")

        print('Opened sheet.')
        logging.info(':: GOOGLESHEET :: Opened sheet.')


    def insert_data(self, smallcases):
        for smallcase in smallcases:
            try:
                self.insert(smallcase)
            except:
                self.__init__()
                self.insert(smallcase)
                print(':: GOOGLESHEET :: Failed. Retrying again.', smallcase.name, ':', smallcase.index)
                logging.info(':: GOOGLESHEET :: Failed. Retrying again. %s : %s', smallcase.name, smallcase.index)



    def insert(self, smallcase):
        try:
            curr_worksheet = self.sheet.worksheet(smallcase.name)
        except:
            print(':: GOOGLESHEET :: Sheet does not exist. Creating worksheet for ', smallcase.name)
            logging.info(':: GOOGLESHEET :: Sheet does not exist. Creating worksheet for %s ', smallcase.name)
            curr_worksheet = self.sheet.add_worksheet(title=smallcase.name, rows=2, cols=5)

        try:
            curr_worksheet = self.sheet.worksheet(smallcase.name)
            curr_worksheet.append_row(smallcase.get_ordered_data())
        except:
            print(':: GOOGLESHEET :: Failed while puttind data for', smallcase.name, ':', smallcase.index)
            logging.info(':: GOOGLESHEET :: Failed while puttind data for %s : %s', smallcase.name, smallcase.index)

        print(':: GOOGLESHEET ::', smallcase.name, ':', smallcase.index)
        logging.info(':: GOOGLESHEET :: %s : %s', smallcase.name, smallcase.index)

        return True


