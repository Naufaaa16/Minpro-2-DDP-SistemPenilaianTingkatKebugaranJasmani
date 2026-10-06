import pwinput
import os
import math
import time

akun = {
    "admin": {"password": "mantap321", "role": "admin"},
    "user": {"password": "keren123", "role": "user"}
}
data_peserta = []

def login(username, password):
    if username in akun and akun[username]["password"] == password:
        return True
    else:
        return False

def input_skor(jenis_latihan):
    while True:
        try:
            skor = int(input(f"Masukkan skor {jenis_latihan} (0-100): "))
            if 0 <= skor <= 100:
                return skor
            else:
                print("Nilai harus di antara 0-100")
        except ValueError:
            print("Input skor tidak valid, masukkan angka dari 0 hingga 100")

def hitung_rata_rata(push_up, sit_up, lari):
    total = math.fsum([push_up, sit_up, lari])
    rata_rata = total / 3
    return rata_rata

def tentukan_kategori(rata_rata):
    if rata_rata <= 59:
        return "kurang"
    elif 60 <= rata_rata <= 75:
        return "cukup"
    elif 75 <= rata_rata <= 85:
        return "baik"
    else:
        return "sangat baik"

def tambah_data():
    nama = input("Masukkan nama peserta: ")
    push_up = input_skor("push up")
    sit_up = input_skor("sit up")
    lari = input_skor("lari")

    rata_rata = hitung_rata_rata(push_up, sit_up, lari)
    kategori = tentukan_kategori(rata_rata)

    data_peserta.append({
        "nama": nama,
        "push_up": push_up,
        "sit_up": sit_up,
        "lari": lari,
        "rata_rata": rata_rata,
        "kategori": kategori
    })

def hapus_data():
    if len(data_peserta) == 0:
        print("Data belum dimasukkan")
    else:
        for i, peserta in enumerate(data_peserta):
            print(f"{i + 1}. {peserta['nama']}")

        nomor = int(input("Masukkan nomor peserta yang ingin dihapus: "))

        if 1 <= nomor <= len(data_peserta):
            indeks = nomor - 1
            peserta = data_peserta[indeks]
            print(f"Data yang akan dihapus: {peserta}")
            data_peserta.pop(indeks)
            print("Data berhasil dihapus")
        else:
            print("Data peserta tidak ditemukan!")

def lihat_data():
    if len(data_peserta) == 0:
        print("Data belum dimasukkan")
    else:
        print("\n====== DATA PESERTA =====")
        for peserta in data_peserta:
            print(f"Nama: {peserta['nama']}")
            print(f"Push Up: {peserta['push_up']}")
            print(f"Sit Up: {peserta['sit_up']}")
            print(f"Lari: {peserta['lari']}")
            print(f"Rata-rata: {peserta['rata_rata']:.2f}")
            print(f"Kategori: {peserta['kategori']}")

def ubah_data():
    if len(data_peserta) == 0:
        print("Data belum dimasukkan")
    else:
        for i, peserta in enumerate(data_peserta):
            print(f"{i + 1}. {peserta['nama']}")

        nomor = int(input("Masukkan nomor peserta yang ingin diubah: "))

        if 1 <= nomor <= len(data_peserta):
            indeks = nomor - 1
            peserta = data_peserta[indeks]

            print(f"Data saat ini: {peserta}")
            nama_baru = input("Masukkan nama baru: ")
            if nama_baru:
                peserta['nama'] = nama_baru

            push_up_baru = input("Masukkan skor Push Up baru: ")
            if push_up_baru:
                peserta['push_up'] = int(push_up_baru)

            sit_up_baru = input("Masukkan skor Sit Up baru: ")
            if sit_up_baru:
                peserta['sit_up'] = int(sit_up_baru)

            lari_baru = input("Masukkan skor Lari baru: ")
            if lari_baru:
                peserta['lari'] = int(lari_baru)

            rata_rata = hitung_rata_rata(peserta['push_up'], peserta['sit_up'], peserta['lari'])
            kategori = tentukan_kategori(rata_rata)
            peserta['rata_rata'] = rata_rata
            peserta['kategori'] = kategori

            print("Data berhasil diubah")
        else:
            print("Data peserta tidak ditemukan!")

def hapus_data():
    if len(data_peserta) == 0:
        print("Data belum dimasukkan")
    else:
        for i, peserta in enumerate(data_peserta):
            print(f"{i + 1}. {peserta['nama']}")

        nomor = int(input("Masukkan nomor peserta yang ingin dihapus: "))

        if 1 <= nomor <= len(data_peserta):
            indeks = nomor - 1
            peserta = data_peserta[indeks]
            print(f"Data yang akan dihapus: {peserta}")
            data_peserta.pop(indeks)
            print("Data berhasil dihapus")
        else:
            print("Data peserta tidak ditemukan!")

while True:
    os.system("cls") if os.name == "nt" else "clear"
    print("===== SISTEM PENILAIAN TINGKAT KEBUGARAN JASMANI =====")
    percobaan = 0
    while percobaan < 3:
        user = input("Username: ")
        pwd = pwinput.pwinput("Password: ")
        print(f"halo {user}, password anda berisi {len(pwd)} karakter")

        if login(user, pwd):
            print(f"Login berhasil. Selamat datang, {user}!")
            break
        else:
            percobaan += 1
            print(f"Login gagal. Username atau password anda salah. Percobaan ke-{percobaan}/3")

    if login(user, pwd) == False:
        print("Anda telah mencoba login sebanyak 3 kali. Program akan diberhentikan.")
        break

    elif akun[user]["role"] == "admin":
        while True:
            print("===== MENU ADMIN =====")
            print("1. Tambah Data")
            print("2. Hapus Data")
            print("3. Lihat Data")
            print("4. Ubah Data")
            print("5. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                tambah_data()
            elif pilihan == "2":
                hapus_data()
            elif pilihan == "3":
                lihat_data()
            elif pilihan == "4":
                ubah_data()
            elif pilihan == "5":
                print("Terima kasih telah menggunakan program ini.")
                time.sleep(5)
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

    elif akun[user]["role"] == "user":
        while True:
            print("===== MENU =====")
            print("1. Lihat Data")
            print("2. Keluar")

            pilihan = input("Pilih menu: ")

            if pilihan == "1":
                lihat_data()
            elif pilihan == "2":
                print("Terima kasih telah menggunakan program ini.")
                time.sleep(5)
                break
            else:
                print("Pilihan tidak valid. Silakan pilih menu yang tersedia.")

