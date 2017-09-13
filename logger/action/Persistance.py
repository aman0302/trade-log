from logger.action.GoogleSheet import googlesheet


class persistance():
    def persist_smallcase(self, smallcases, sheet_name):
        sheet = googlesheet(sheet_name)
        sheet.insert_smallcase_data(smallcases)