from logger.action.BrowserFactory import browser_factory
from logger.action.ReversePickupExcel import reverse_pickup_excel
from logger.action.EcomExpress import ecom
from logger.utils.Reporter import *
from logger.utils.ExecutablePath import *


class reverse_pickup_ecom_source():
    def __init__(self):
        self.reverse_pickup_excel = reverse_pickup_excel()
        infoReport(":ECOM RVP SOURCE: initialized")

    def pre(self):
        debugReport(':ECOM RVP SOURCE: pre() called')

    def process(self):
        debugReport(':ECOM RVP SOURCE: process() called')

        if self.reverse_pickup_excel.fetch_data(self.data):
            self.browser = browser_factory().get_browser()
            self.ecom = ecom(self.browser)
            self.ecom.login_and_upload(get_reverse_pickup_excel_file_location(), True)

    def post(self):
        debugReport(':ECOM RVP SOURCE: post() called')
        self.browser.quit()

    def start(self):
        self.pre()
        self.process()
        self.post()

    def pass_value(self, data):
        self.data = data
