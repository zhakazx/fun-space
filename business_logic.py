# (Domain) business_logic.py
from data_access import DataAccess

class ProductService:
    def __init__(self):
        self.access = DataAccess()

    def list_products(self):
        return self.access.fetch_all_products()

    def get_product_detail(self, product_id):
        return self.access.fetch_product(product_id)
