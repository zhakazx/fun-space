# data_access.py
from database import Database

class DataAccess:
    def __init__(self):
        self.db = Database()

    def fetch_product(self, product_id):
        return self.db.get_product(product_id)

    def fetch_all_products(self):
        return self.db.get_all_products()
