import requests, json

from logger.utils.ExecutablePath import *


class shopify_orders:
    def __init__(self):
        with open(get_credentials_path()) as data_file:
            self.credentials = json.load(data_file)
        self.api_key = self.credentials['shopify']['api_key']
        self.password = self.credentials['shopify']['password']

    def get_all_recent_orders(self):
        url = "https://" + self.api_key + ":" + self.password + "@shop-untung.myshopify.com/admin/orders.json?status=any"
        response = requests.request("GET", url)
        return response.json()

    def get_order(self, order_id):
        url = "https://" + self.api_key + ":" + self.password + "@shop-untung.myshopify.com/admin/orders/" + order_id + ".json"
        response = requests.request("GET", url)
        return response.json()
