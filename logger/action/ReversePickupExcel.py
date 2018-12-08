import xlsxwriter

from logger.utils.Reporter import *
from logger.utils.ExecutablePath import *
from logger.action.ShopifyOrders import shopify_orders


class reverse_pickup_excel:
    def __init__(self):
        self.shopify = shopify_orders()
        self.workbook = xlsxwriter.Workbook(get_reverse_pickup_excel_file_location())
        self.worksheet = self.workbook.add_worksheet()
        self.default_values = []
        column = 0
        with open(get_reverse_pickup_excel_file_heading()) as data_file:
            for line in data_file.readlines():
                self.worksheet.write(0, column, line.split("|")[0].strip())
                column += 1
                if len(line.split("|")) > 1:
                    self.default_values.append(line.split("|")[1].strip())
                else:
                    self.default_values.append("")

    def fetch_data(self, data):
        upload_needed = False

        infoReport(":UPLOAD EXCEL: Processing Order Number - " + str(data))
        self.default_values[0] = awb_number = int(data["awb"])
        self.default_values[1] = order_id = int(data["order_id"])
        self.default_values[2] = product = "REV"
        self.default_values[3] = name = data["name"]
        self.default_values[4] = add1 = data["address1"]
        self.default_values[5] = add2 = data["address2"]
        self.default_values[7] = city = data["city"]
        self.default_values[8] = pincode = data["pin"]
        self.default_values[9] = state = data["state"]
        self.default_values[10] = mobile = (str(data["mobile"])).strip().lstrip("0").replace(" ", "").replace("+91", "")
        self.default_values[12] = data["description"]
        self.default_values[13] = pieces = int(data["pieces"])
        self.default_values[15] = decalred_value = data["value"]
        self.default_values[16] = total_weight = int(data["weight"])
        self.default_values[27] = drop_mobile = 8197740003


        for index, item in enumerate(self.default_values):
            self.worksheet.write(1, index, item)

        self.workbook.close()

        if (data["awb"] == "" or data["pieces"] == "" or data["value"] == "" or data["weight"] == ""):
            upload_needed = False
        else:
            upload_needed = True
        return upload_needed
