from prettytable import PrettyTable

class Admin:
    def _init_(self):
        self.products = []

    def create_product(self, name, price):
        product = {'name': name, 'price': price}
        self.products.append(product)
        print(f"Produk {name} berhasil ditambahkan.")

    def read_products(self):
        if not self.products:
            print("Belum ada produk yang tersedia.")
        else:
            table = PrettyTable(['No', 'Nama Produk', 'Harga'])
            for idx, product in enumerate(self.products, 1):
                table.add_row([idx, product['name'], f"Rp {product['price']}"])
            print(table)

    def update_product(self, idx, name, price):
        if 1 <= idx <= len(self.products):
            self.products[idx - 1]['name'] = name
            self.products[idx - 1]['price'] = price
            print(f"Produk {name} berhasil diperbarui.")
        else:
            print("Indeks produk tidak valid.")

    def delete_product(self, idx):
        if 1 <= idx <= len(self.products):
            deleted_product = self.products.pop(idx - 1)
            print(f"Produk {deleted_product['name']} berhasil dihapus.")
        else:
            print("Indeks produk tidak valid.")

class Pembeli:
    def _init_(self):
        self.cart = []

    def add_to_cart(self, product):
        self.cart.append(product)
        print(f"Produk {product['name']} ditambahkan ke keranjang.")

    def view_cart(self):
        if not self.cart:
            print("Keranjang kosong.")
        else:
            table = PrettyTable(['No', 'Nama Produk', 'Harga'])
            for idx, product in enumerate(self.cart, 1):
                table.add_row([idx, product['name'], f"Rp {product['price']}"])
            print(table)

    def checkout(self):
        if not self.cart:
            print("Keranjang kosong. Tidak ada yang bisa di-checkout.")
            return
        
        total = sum(product['price'] for product in self.cart)
        print(f"Total harga: Rp {total}")
        
        while True:
            try:
                bayar = float(input("Masukkan jumlah uang yang dibayarkan: Rp "))
                if bayar < total:
                    print("Jumlah uang yang dibayarkan kurang dari total harga.")
                else:
                    kembalian = bayar - total
                    print(f"Uang kembalian: Rp {kembalian}")
                    self.cart.clear()
                    print("Keranjang dikosongkan. Terima kasih telah berbelanja!")
                    break
            except ValueError:
                print("Masukkan jumlah uang yang valid.")


admin = Admin()
pembeli = Pembeli()


admin.create_product("Teddy Bear", 60000)
admin.create_product("Robot", 50000)
admin.create_product("Puzzle", 15000)

while True:
    print("\nMenu Utama:")
    print("1. Masuk sebagai Admin")
    print("2. Masuk sebagai Pembeli")
    print("3. Keluar")
    choice = input("Pilih peran Anda (1/2/3): ")

    if choice == '1':
        while True:
            print("\nMenu Admin:")
            print("1. Tambah Produk")
            print("2. Lihat Produk")
            print("3. Perbarui Produk")
            print("4. Hapus Produk")
            print("5. Kembali ke Menu Utama")
            admin_choice = input("Pilih tindakan Admin (1/2/3/4/5): ")

            if admin_choice == '1':
                name = input("Masukkan nama produk: ")
                price = float(input("Masukkan harga produk: "))
                admin.create_product(name, price)
            elif admin_choice == '2':
                admin.read_products()
            elif admin_choice == '3':
                admin.read_products()
                idx = int(input("Masukkan indeks produk yang akan diperbarui: "))
                name = input("Masukkan nama produk baru: ")
                price = float(input("Masukkan harga produk baru: "))
                admin.update_product(idx, name, price)
            elif admin_choice == '4':
                admin.read_products()
                idx = int(input("Masukkan indeks produk yang akan dihapus: "))
                admin.delete_product(idx)
            elif admin_choice == '5':
                break

    elif choice == '2':
        while True:
            print("\nMenu Pembeli:")
            print("1. Tambahkan Produk ke Keranjang")
            print("2. Lihat Keranjang")
            print("3. Checkout")
            print("4. Kembali ke Menu Utama")
            pembeli_choice = input("Pilih tindakan Pembeli (1/2/3/4): ")

            if pembeli_choice == '1':
                admin.read_products()
                idx = int(input("Masukkan indeks produk yang ingin Anda beli: "))
                product = admin.products[idx - 1]
                pembeli.add_to_cart(product)
            elif pembeli_choice == '2':
                pembeli.view_cart()
            elif pembeli_choice == '3':
                pembeli.checkout()
            elif pembeli_choice == '4':
                break

    elif choice == '3':
        break
    else:
        print("Pilihan tidak valid. Silakan pilih kembali.")