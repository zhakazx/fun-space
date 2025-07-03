# interface_terminal.py
class TerminalUI:
    @staticmethod
    def show_products(products):
        print("\nDaftar Produk:")
        for id, info in products.items():
            print(f"{id}. {info['name']} - Rp{info['price']}")

    @staticmethod
    def show_product_detail(product):
        if product:
            print(f"Nama: {product['name']}")
            print(f"Harga: Rp{product['price']}")
        else:
            print("Produk tidak ditemukan.")
