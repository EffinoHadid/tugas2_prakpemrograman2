class Produk:

    def __init__(self, nama_produk, harga_produk):
        self.nama_produk = nama_produk
        self.harga_produk = harga_produk

    def hitung_total(self, jumlah_beli):
        return self.harga_produk * jumlah_beli

    def hitung_diskon(self, total_seluruh):
        if total_seluruh > 5000:
            return total_seluruh * 0.05
        else:
            return 0


print("Data Produk:")
nama = input("Nama produk : ")
harga = int(input("Harga produk: "))
jumlah = int(input("Jumlah beli : "))

produk_obj = Produk(nama, harga)
total_seluruh = produk_obj.hitung_total(jumlah)

diskon = produk_obj.hitung_diskon(total_seluruh)
total_bayar = total_seluruh - diskon

print("\n=== HASIL PEMBELIAN ===")
print(f"Total Pembelian: Rp{int(total_seluruh)}")
print(f"Diskon 5% : Rp{int(diskon)}")
print(f"Total Bayar : Rp{int(total_bayar)}")