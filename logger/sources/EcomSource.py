from logger.action.BrowserFactory import browser_factory
from logger.action.UploadExcel import upload_excel
from logger.action.EcomExpress import ecom
from logger.utils.Reporter import *
from logger.utils.ExecutablePath import *


class ecom_source():
    def __init__(self):
        self.upload_excel = upload_excel()
        infoReport(":ECOM SOURCE: initialized")

    def pre(self):
        debugReport(':ECOM SOURCE: pre() called')

    def process(self):
        debugReport(':ECOM SOURCE: process() called')

        if self.is_shopify:
            if self.upload_excel.fetch_data(self.selected_list):
                self.browser = browser_factory().get_browser()
                self.ecom = ecom(self.browser)
                self.ecom.login_and_upload(get_upload_excel_file_location(), False)

        else:
            if self.upload_excel.create_excel(self.data):
                self.browser = browser_factory().get_browser()
                self.ecom = ecom(self.browser)
                self.ecom.login_and_upload(get_upload_excel_file_location(), False)

    def post(self):
        debugReport(':ECOM SOURCE: post() called')
        self.browser.quit()

    def start(self):
        self.pre()
        self.process()
        self.post()

    def pass_value(self, data):
        self.data = data
        self.is_shopify = False

    def pass_value_shopify(self, selected_list, is_shopify):
        self.is_shopify = is_shopify
        self.selected_list = selected_list
