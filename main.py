# main.py
from interface_terminal import TerminalUI
from business_logic import ProductService

def login():
    valid_username = "admin"
    valid_password = "123"
    attempts = 0

    while attempts < 3:
        username = input("Username: ")
        password = input("Password: ")
 
        if not username or not password:
            print("Username dan/atau password tidak boleh kosong.\n")
        elif username == valid_username and password == valid_password:
            print("Login berhasil!\n")
            return True
        elif username == valid_username:
            print("Password salah.\n")
        elif password == valid_password:
            print("Username salah.\n")
        else:
            print("Username dan password salah.\n")
        attempts += 1

    print("Percobaan login gagal lebih dari 3 kali.")
    return False

def main():
    if not login():
        return
    
    service = ProductService()
    ui = TerminalUI()

    while True:
        print("\n1. Lihat semua produk")
        print("2. Lihat detail produk")
        print("3. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            products = service.list_products()
            ui.show_products(products)
        elif pilihan == "2":
            pid = input("Masukkan ID produk: ")
            detail = service.get_product_detail(pid)
            ui.show_product_detail(detail)
        elif pilihan == "3":
            print("Keluar dari program.")
            break
        else:
            print("Menu tidak valid.")

if __name__ == "__main__":
    main()
