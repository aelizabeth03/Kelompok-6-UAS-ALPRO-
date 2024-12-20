# Sistem Pencatatan Stok Barang di Gudang

stok_barang = {}

# menampilkan menu
def main_menu():
    print("SELAMAT DATANG DI GUDANG CAL!")
    while True:
        print("\n=== Menu Utama ===")
        print("1. Tambah Barang Baru ke Stok")
        print("2. Hapus Barang dari Stok")
        print("3. Perbarui Jumlah Barang")
        print("4. Keluar")

        pilihan = input("Pilih menu (1-4): ")

        if pilihan == "1":
            tambah_barang()
        elif pilihan == "2":
            hapus_barang()
        elif pilihan == "3":
            perbarui_stok()
        elif pilihan == "4":
            print("Program Stok Barang Telah Selesai!")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

#menambah barang baru
def tambah_barang():
    nama = input("Masukkan nama barang: ")
    if nama in stok_barang:
        print(f"Barang '{nama}' sudah ada dalam stok.")
        return
    try:
        jumlah = int(input("Masukkan jumlah stok awal: "))
        stok_barang[nama] = jumlah
        print(f"Barang '{nama}' berhasil ditambahkan dengan jumlah {jumlah}.")
    except ValueError:
        print("Input jumlah harus berupa angka.")

#menghapus barang dari stok
def hapus_barang():
    nama = input("Masukkan nama barang yang akan dihapus: ")
    if nama in stok_barang:
        del stok_barang[nama]
        print(f"Barang '{nama}' berhasil dihapus dari stok.")
    else:
        print(f"Barang '{nama}' tidak ditemukan dalam stok.")

#memperbarui jumlah stok barang
def perbarui_stok():
    nama = input("Masukkan nama barang yang akan diperbarui: ")
    if nama in stok_barang:
        try:
            jumlah = int(input("Masukkan jumlah stok baru: "))
            stok_barang[nama] = jumlah
            print(f"Stok barang '{nama}' diperbarui menjadi {jumlah}.")
        except ValueError:
            print("Input jumlah harus berupa angka.")
    else:
        print(f"Barang '{nama}' tidak ditemukan dalam stok.")

#mencari barang berdasarkan nama
def cari_barang():
    nama = input("Masukkan nama barang yang dicari: ")
    if nama in stok_barang:
        print(f"Barang '{nama}' ditemukan dengan jumlah stok {stok_barang[nama]}.")
    else:
        print(f"Barang '{nama}' tidak ditemukan dalam stok.")

#menampilkan barang dengan stok di bawah jumlah tertentu
def tampilkan_barang_bawah_stok():
    try:
        batas = int(input("Masukkan batas jumlah stok: "))
        print(f"\nBarang dengan stok di bawah {batas}:")
        ditemukan = False
        for nama, jumlah in stok_barang.items():
            if jumlah < batas:
                print(f"- {nama}: {jumlah}")
                ditemukan = True
        if not ditemukan:
            print("Tidak ada barang dengan stok di bawah batas yang diberikan.")
    except ValueError:
        print("Input batas jumlah harus berupa angka.")
        
if __name__ == "__main__":
    main_menu() 
