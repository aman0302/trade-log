from tkinter import *
import Pmw

from logger.action.ShopifyOrders import shopify_orders
from logger.sources.EcomSource import ecom_source


class ui_action(Frame):
    def __init__(self):
        Frame.__init__(self)

        self.shopify = shopify_orders()
        self.shopify_orders = []
        self.order_list = self.get_order_ids()
        self.selected_list = []
        self.awb_list=[]

        self.pack(expand=YES, fill=BOTH)
        self.master.title("Magic Machine")
        self.order_list_box = Pmw.ScrolledListBox(self,
                                                  items=self.order_list,
                                                  listbox_height=20,
                                                  vscrollmode="static",
                                                  listbox_selectmode=EXTENDED)
        self.order_list_box.pack(side=LEFT, expand=YES, fill=BOTH, padx=15, pady=15)

        self.add_button = Button(self, text=">>>", command=self.add_order)
        self.add_button.pack(side=LEFT, padx=15, pady=15)

        self.removeButton = Button(self, text="<<<", command=self.remove_order)
        self.removeButton.pack(side=LEFT, padx=15, pady=15)

        self.submit_button = Button(self, text="Submit", command=self.submit)
        self.submit_button.pack(side=BOTTOM, padx=15, pady=15)

        self.confirm_button = Button(self, text="Confirm Orders", command=self.confirm_orders)
        self.confirm_button.pack(side=BOTTOM, padx=15, pady=15)

        self.selected_list_box = Pmw.ScrolledListBox(self,
                                                     items=(),
                                                     listbox_height=20,
                                                     vscrollmode="static",
                                                     listbox_selectmode=EXTENDED)
        self.selected_list_box.pack(side=LEFT, expand=YES, fill=BOTH, padx=15, pady=15)

        self.texbox = Text(self)
        self.texbox.pack(side=TOP, padx=15, pady=15)

        self.awb_texbox = Text(self)
        self.awb_texbox.pack(side=TOP, padx=15, pady=15)

    def add_order(self):
        selected = self.order_list_box.getcurselection()
        if selected:
            for item in selected:
                self.selected_list_box.insert(0, item)

        pos = 0
        selected_index = self.order_list_box.curselection()
        if selected_index:
            for item in selected_index:
                idx = int(item) - pos
                self.order_list_box.delete(idx, idx)
                pos = pos + 1

    def remove_order(self):
        selected = self.selected_list_box.getcurselection()
        if selected:
            for item in selected:
                self.order_list_box.insert(0, item)

        pos = 0
        selected_index = self.selected_list_box.curselection()
        if selected_index:
            for item in selected_index:
                idx = int(item) - pos
                self.selected_list_box.delete(idx, idx)
                pos = pos + 1

    def get_order_ids(self):
        order_ids = []
        self.shopify_orders = self.shopify.get_all_recent_orders()["orders"]
        for order in self.shopify_orders:
            order_ids.append(order["order_number"])
        order_ids.sort(reverse=True)
        return order_ids

    def confirm_orders(self):
        self.texbox.delete(1.0, END)
        self.awb_texbox.delete(1.0, END)
        details = []
        # for order in self.shopify_orders:
        self.selected_list = list(self.selected_list_box.get(0, END))
        for order_id in self.selected_list:
            for order in self.shopify.get_all_recent_orders()["orders"]:
                phone = str(order["shipping_address"]["phone"]).strip().lstrip("0").replace(" ", "").replace("+91", "")
                if order["order_number"] == order_id:
                    payment_gateway = order["payment_gateway_names"]
                    if "cash_on_delivery" in payment_gateway:
                        product = "COD"
                    else:
                        product = "PPD"

                    tracking_number=str(order["fulfillments"][0]["tracking_number"])
                    detail = str(order["order_number"]) + " -> " +tracking_number + " -> " + product + " -> " + phone + " -> " + str(order["shipping_address"]["name"]) + "\n"
                    details.append(detail)
                    self.texbox.insert(INSERT, detail)
                    self.awb_texbox.insert(INSERT, tracking_number+",")
                    break

    def get_selected_orders(self):
        return self.selected_list

    def submit(self):
        self.ecom = ecom_source()
        self.ecom.pass_value(self.selected_list)
        self.ecom.start()
