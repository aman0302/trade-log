from tkinter import *
from tkinter import ttk
import Pmw

from logger.utils.ExecutablePath import *
from logger.action.ShopifyOrders import shopify_orders
from logger.sources.EcomSource import ecom_source
from logger.sources.ReversePickupEcomSource import reverse_pickup_ecom_source


class ui_action(Frame):
    def __init__(self):
        self.shopify = shopify_orders()

        self.root = Tk()
        notebook = ttk.Notebook(self.root)

        self.tab1 = ttk.Frame(notebook)  # first page, which would get widgets gridded into it
        notebook.add(self.tab1, text='Shopify')
        self.makeTab1()

        self.tab2 = ttk.Frame(notebook)  # second page
        notebook.add(self.tab2, text='Reverse Pickup')
        self.makeTab2()

        notebook.grid()
        self.root.mainloop()

    def makeTab1(self):
        self.shopify_orders = []
        self.order_list = self.get_order_ids()
        self.selected_list = []
        self.awb_list = []

        self.order_list_box = Pmw.ScrolledListBox(self.tab1, items=self.order_list, listbox_height=10,
                                                  vscrollmode="static", listbox_selectmode=EXTENDED)
        self.order_list_box.grid(row=0, column=0)

        add_remove_frame = Frame(self.tab1)
        add_remove_frame.grid(row=0, column=1)

        add_button = Button(add_remove_frame, text=">>>", command=self.add_order)
        add_button.pack()

        removeButton = Button(add_remove_frame, text="<<<", command=self.remove_order)
        removeButton.pack()

        confirm_submit_frame = Frame(self.tab1)
        confirm_submit_frame.grid(row=1, column=1)

        confirm_button = Button(confirm_submit_frame, text="Confirm Orders", command=self.confirm_orders)
        confirm_button.pack()

        submit_button = Button(confirm_submit_frame, text="Proceed to ECOM", command=self.submit)
        submit_button.pack()

        self.selected_list_box = Pmw.ScrolledListBox(self.tab1, items=(), listbox_height=10, vscrollmode="static",
                                                     listbox_selectmode=EXTENDED)
        self.selected_list_box.grid(row=0, column=2)

        self.texbox = Text(self.tab1, height=10)
        self.texbox.grid(row=0, column=3)

        self.awb_texbox = Text(self.tab1, height=10)
        self.awb_texbox.grid(row=1, column=3)

    def makeTab2(self):
        oidt = StringVar()
        oidt.set("Order ID")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=0, column=0)
        self.reverse_order_id = Entry(self.tab2)
        self.reverse_order_id.grid(row=0, column=1)

        oidt = StringVar()
        oidt.set("AWB Number")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=1, column=0)
        self.reverse_awb = Entry(self.tab2)
        self.reverse_awb.grid(row=1, column=1)

        oidt = StringVar()
        oidt.set("Name")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=2, column=0)
        self.reverse_name = Entry(self.tab2)
        self.reverse_name.grid(row=2, column=1)

        oidt = StringVar()
        oidt.set("Address 1")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=3, column=0)
        self.reverse_add1 = Entry(self.tab2)
        self.reverse_add1.grid(row=3, column=1)

        oidt = StringVar()
        oidt.set("Address 2")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=4, column=0)
        self.reverse_add2 = Entry(self.tab2)
        self.reverse_add2.grid(row=4, column=1)

        oidt = StringVar()
        oidt.set("Address 3")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=5, column=0)
        self.reverse_add3 = Entry(self.tab2)
        self.reverse_add3.grid(row=5, column=1)

        oidt = StringVar()
        oidt.set("City")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=6, column=0)
        self.reverse_city = Entry(self.tab2)
        self.reverse_city.grid(row=6, column=1)

        oidt = StringVar()
        oidt.set("Pin")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=7, column=0)
        self.reverse_pin = Entry(self.tab2)
        self.reverse_pin.grid(row=7, column=1)

        oidt = StringVar()
        oidt.set("State")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=8, column=0)
        self.reverse_state = Entry(self.tab2)
        self.reverse_state.grid(row=8, column=1)

        oidt = StringVar()
        oidt.set("Mobile")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=9, column=0)
        self.reverse_mobile = Entry(self.tab2)
        self.reverse_mobile.grid(row=9, column=1)

        oidt = StringVar()
        oidt.set("Description")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=10, column=0)
        self.reverse_desc = Entry(self.tab2)
        self.reverse_desc.grid(row=10, column=1)

        oidt = StringVar()
        oidt.set("Number of Pieces")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=11, column=0)
        self.reverse_pieces = Entry(self.tab2)
        self.reverse_pieces.grid(row=11, column=1)

        oidt = StringVar()
        oidt.set("Declared Value")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=12, column=0)
        self.reverse_dec_value = Entry(self.tab2)
        self.reverse_dec_value.grid(row=12, column=1)

        oidt = StringVar()
        oidt.set("Weight")
        oidl = Label(self.tab2, textvariable=oidt)
        oidl.grid(row=13, column=0)
        self.reverse_dec_weight = Entry(self.tab2)
        self.reverse_dec_weight.grid(row=13, column=1)

        confirm_button = Button(self.tab2, text="Confirm Orders", command=self.reverse_confirm_orders)
        confirm_button.grid(row=14, column=0)

        assign_awb = Button(self.tab2, text="Assign AWB", command=self.reverse_assign_awb)
        assign_awb.grid(row=15, column=0)

        reverse_submit_button = Button(self.tab2, text="Proceed to ECOM", command=self.reverse_submit)
        reverse_submit_button.grid(row=15, column=1)

        self.order_items = Text(self.tab2, height=5)
        self.order_items.grid(row=0, column=2)

        self.summary = Text(self.tab2, height=2)
        self.summary.grid(row=2, column=2)

    def get_order_ids(self):
        order_ids = []
        self.shopify_orders = self.shopify.get_all_recent_orders()["orders"]
        for order in self.shopify_orders:
            order_ids.append(order["order_number"])
        order_ids.sort(reverse=True)
        return order_ids

    def get_selected_orders(self):
        return self.selected_list

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

                    tracking_number = str(order["fulfillments"][0]["tracking_number"])
                    detail = str(order[
                                     "order_number"]) + " -> " + tracking_number + " -> " + product + " -> " + phone + " -> " + str(
                        order["shipping_address"]["name"]) + "\n"
                    details.append(detail)
                    self.texbox.insert(INSERT, detail)
                    self.awb_texbox.insert(INSERT, tracking_number + ",")
                    break

    def reverse_confirm_orders(self):

        self.reverse_name.delete(0, END)
        self.reverse_add1.delete(0, END)
        self.reverse_add2.delete(0, END)
        self.reverse_city.delete(0, END)
        self.reverse_pin.delete(0, END)
        self.reverse_state.delete(0, END)
        self.reverse_mobile.delete(0, END)
        self.reverse_pieces.delete(0, END)
        self.reverse_dec_value.delete(0, END)
        self.reverse_dec_weight.delete(0, END)
        self.order_items.delete(1.0, END)
        self.summary.delete(1.0, END)

        for order in self.shopify.get_all_recent_orders()["orders"]:
            # print(order,self.reverse_order_id.get(),order["order_number"])
            if order["order_number"] == int(self.reverse_order_id.get()):
                # print(order)
                self.reverse_name.insert(0, order["shipping_address"]["first_name"] + " " + order["shipping_address"][
                    "last_name"])
                self.reverse_add1.insert(0, order["shipping_address"]["address1"])
                self.reverse_add2.insert(0, order["shipping_address"]["address2"])
                self.reverse_city.insert(0, order["shipping_address"]["city"])
                self.reverse_pin.insert(0, order["shipping_address"]["zip"])
                self.reverse_state.insert(0, order["shipping_address"]["province"])
                phone = str(order["shipping_address"]["phone"]).strip().lstrip("0").replace(" ", "").replace("+91", "")
                self.reverse_mobile.insert(0, phone)

                details = ""
                for item in order["line_items"]:
                    detail = str(item["title"] + " - " + item["sku"] + " - " + item["price"]) + "\n"
                    details += detail

                self.order_items.insert(INSERT, details)

                awb = self.reverse_assign_awb()

                payment_gateway = order["payment_gateway_names"]
                if "cash_on_delivery" in payment_gateway:
                    product = "COD"
                else:
                    product = "PPD"

                summary_text = awb + "\t" + str(order["order_number"]) + "\t" + order["shipping_address"][
                    "city"] + "\t" + product + "\t" + order["shipping_address"]["first_name"] + " " + \
                               order["shipping_address"][
                                   "last_name"] + "\t" + phone

                self.summary.insert(INSERT, summary_text)

    def submit(self):
        self.ecom = ecom_source()
        self.ecom.pass_value(self.selected_list)
        self.ecom.start()

    def reverse_submit(self):
        data = {}
        data["awb"] = self.reverse_awb.get()
        data["order_id"] = self.reverse_order_id.get()
        data["name"] = self.reverse_name.get()
        data["address1"] = self.reverse_add1.get()
        data["address2"] = self.reverse_add2.get()
        data["city"] = self.reverse_city.get()
        data["pin"] = self.reverse_pin.get()
        data["state"] = self.reverse_state.get()
        data["mobile"] = self.reverse_mobile.get()
        data["description"] = self.reverse_desc.get()
        data["pieces"] = self.reverse_pieces.get()
        data["value"] = self.reverse_dec_value.get()
        data["weight"] = self.reverse_dec_weight.get()

        self.reverse_ecom = reverse_pickup_ecom_source()
        self.reverse_ecom.pass_value(data)
        self.reverse_ecom.start()

        lines = []
        with open(get_reverse_pickup_awb_file_location(), 'r') as awbs:
            lines = awbs.readlines()

        with open(get_reverse_pickup_awb_file_location(), 'w') as awbs:
            awbs.writelines([item for item in lines[:-1]])

    def reverse_assign_awb(self):
        self.reverse_awb.delete(0, END)
        with open(get_reverse_pickup_awb_file_location(), 'r') as awbs:
            lines = awbs.read().splitlines()
            last_line = lines[-1]
            self.reverse_awb.insert(0, last_line)
            return last_line
