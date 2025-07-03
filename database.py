# database.py
# Simulasi koneksi database (dummy)
class Database:
    def __init__(self):
        self.data = {"1": {"name": "Produk A", "price": 10000},
                     "2": {"name": "Produk B", "price": 20000}}

    def get_product(self, product_id):
        return self.data.get(product_id)

    def get_all_products(self):
        return self.data
