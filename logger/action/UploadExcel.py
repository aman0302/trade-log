import xlsxwriter

from logger.utils.Reporter import *
from logger.utils.ExecutablePath import *
from logger.action.ShopifyOrders import shopify_orders


class upload_excel:
    def __init__(self):
        self.shopify = shopify_orders()
        self.workbook = xlsxwriter.Workbook(get_upload_excel_file_location())
        self.worksheet = self.workbook.add_worksheet()
        self.default_values = []
        column = 0
        with open(get_excel_file_heading()) as data_file:
            for line in data_file.readlines():
                self.worksheet.write(0, column, line.split("|")[0])
                column += 1
                if len(line.split("|")) > 1:
                    self.default_values.append(line.split("|")[1])
                else:
                    self.default_values.append("")

    def fetch_data(self, order_ids):
        upload_needed = False
        row = 0
        order_list = self.shopify.get_all_recent_orders()["orders"];
        for order_id in order_ids:
            for order in order_list:
                if int(order["order_number"]) == int(order_id):
                    row += 1
                    infoReport(
                        ":UPLOAD EXCEL: Processing Order Number - " + str(order_id) + " added to row " + str(row))
                    upload_needed = True

                    self.default_values[0] = awb_number = order["fulfillments"][0]["tracking_number"]
                    self.default_values[1] = order_id = order["order_number"]

                    payment_gateway = order["payment_gateway_names"]
                    # print(payment_gateway)
                    if "cash_on_delivery" in payment_gateway:
                        self.default_values[2] = product = "COD"
                    else:
                        self.default_values[2] = product = "PPD"

                    self.default_values[3] = name = order["shipping_address"]["name"]
                    self.default_values[4] = add1 = order["shipping_address"]["address1"]
                    self.default_values[5] = add2 = order["shipping_address"]["address2"]
                    self.default_values[7] = city = order["shipping_address"]["city"]
                    self.default_values[8] = pincode = order["shipping_address"]["zip"]
                    self.default_values[9] = state = order["shipping_address"]["province"]
                    self.default_values[10] = mobile = (str(order["shipping_address"][
                                                                "phone"])).strip().lstrip("0").replace(" ", "").replace(
                        "+91", "")
                    self.default_values[12] = "Women Apparel"
                    self.default_values[13] = pieces = (len(order["line_items"]))

                    if product == "COD":
                        self.default_values[14] = total_price = order["total_price"]
                    else:
                        self.default_values[14] = total_price = 0

                    self.default_values[15] = decalred_value = 1900 * pieces
                    self.default_values[16] = total_weight = order["total_weight"]

                    if total_weight > 500 and total_weight <= 600:
                        self.default_values[16] = total_weight = 500

                    for index, item in enumerate(self.default_values):
                        self.worksheet.write(row, index, item)

        self.workbook.close()
        return upload_needed

    def create_excel(self, data):
        upload_needed = False

        self.default_values[0] = awb_number = data["awb"]
        self.default_values[1] = order_id = data["order_id"]
        self.default_values[2] = product = data["product"]
        self.default_values[3] = name = data["name"]
        self.default_values[4] = add1 = data["address1"]
        self.default_values[5] = add2 = data["address2"]
        self.default_values[7] = city = data["city"]
        self.default_values[8] = pincode = data["pin"]
        self.default_values[9] = state = data["state"]
        self.default_values[10] = mobile = data["mobile"]
        self.default_values[12] = description = data["description"]
        self.default_values[13] = pieces = data["pieces"]
        self.default_values[15] = dec_price = data["value"]
        self.default_values[14] = col_value = data["collectible"]
        self.default_values[16] = total_weight = data["weight"]

        for index, item in enumerate(self.default_values):
            self.worksheet.write(1, index, item)

        upload_needed = True
        self.workbook.close()
        return upload_needed
