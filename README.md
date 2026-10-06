# Minpro-2-DDP-SistemPenilaianTingkatKebugaranJasmani

NAMA: NAUFA FAUZA EKY
NIM: 2609116060
KELAS: B
JUDUL MINPRO: SISTEM PENILAIAN TINGKAT KEBUGARAN JASMANI

Note: maaf mba dan abang jika terlihat kurang rapi, saya sudah berusaha selengkap, serapi mungkin untuk penjelasannya, dan saya ada nambahin keterangan line nya di subbab juga ya abang dan mba Terimakasihh

SISTEM PENILAIAN TINGKAT KEBUGARAN JASMANI

  Jadi sistem ini mencatat dan menilai hasil tes kebugaran peserta. Setiap peserta memiliki nama dan tiga skor tes kebugaran, yaitu push up, sit up, dan lari (masing-masing skor bernilai 0-100), lalu program menghitung rata-ratanya dan menentukan kategori kebugarannya: kurang, cukup, baik, atau sangat baik. Akses dibagi dua role lewat login: 
1. admin 
Disini admin dapat menambah, melihat, mengubah, dan menghapus data peserta. 
2. user 
User biasa hanya dapat melihat data yang sudah dimasukkan admin. 

Program ini menggunakan function untuk kode untuk masing masing pilihan menu, dictionary untuk menyimpan akun dan data peserta, serta library pwinput untuk input password, os untuk merapikan layar, dan math untuk menghitung nilai, time untuk jeda sebelum kembali ke halaman login semula.

1. FLOWCHART
   <img width="1600" height="1476" alt="WhatsApp Image 2026-10-06 at 18 50 12" src="https://github.com/user-attachments/assets/80c5f069-6875-4aa7-90e9-f41ef3a7f056" />
   dimulai dari menginput username dan password, jika akun tersimpan di data base maka akan lanjut ke proses berikutnya, jika tidak login akan gagal dan diberi kesempatan 3 kali sebelum program otomatis selesai. Sistem ini mempunyai 2 role untuk login, jika admin login maka admin akan mendapat 5 pilihan di menu yaitu, tambah data, hapus data, lihat data, ubah data, keluar. Sedangkan jika user biasa yang login maka akan tertampil 2 pilihan di menu yaitu lihat data dan keluar.

   berikut ini penjelasan alur program
A. admin
      jika admin memilih pilihan no 1: admin akan menginput nama dan 3 skor lalu program akan memeriksa apakah skor dalam rentang 1-100 jika ya maka program akan menghitung rata-rata dan menentukan kategori nilai dan setelah itu program akan menyimpan data          yang sudah di input, jika rentang nilai yang diinput bukan 1-100 maka program akan menyarankan dan mengarahkan admin untuk            menginput ulang.
      
      jika admin memilih pilihan no 2: admin akan diarahkan untuk melihat tampilan data yang sudah tersimpan (berisi nama dan no peserta), lalu admin menginput no peserta yang ingin dihapus, program akan menghapus data dan akan menampilkan tulisan data berhasil dihapus.
      
      jika admin memilih pilihan no 3: admin akan melihat data yang sudah tersimpan.

      jika admin memilih pilihan no 4: admin akan melihat tampilan daftar nomor dan nama peserta lalu admin akan menginput nama dan skor peserta ulang, lalu program juga akan menghitung rata rata nilai dan menyesuaikan kategori nilai peserta.
      
B. User biasa
      jika user memilih pilihan no 1: user akan otomatis melihat data peserta yang berisikan nama, 3 skor, rata-rata, kategori.
      jika user memilih pilihan no 2: program akan selesai dan menampilkan output terima kasih

2. KODE PROGRAM
   Berikut ini penjelasan kode program beserta penjelasannya
A. Penggunaan Library (line 1-4 python)
   import pwinput
   import os
   import math
   import time

   jadi kode diatas merupakan penggunaan library. import pwinput digunakan untuk    menyembunyikan password saat diketik, import os digunakan agar bisa merapikan output, import math digunakan untuk menghitung rata-rata nilai, import time      digunakan untuk jeda diantara program selesai hingga kembali semula ke laman login

B. Menyimpan data akun login dan data peserta (line 6-10 python)
   akun = {
    "admin": {"password": "mantap321", "role": "admin"},
    "user": {"password": "keren123", "role": "user"}
  }
  data_peserta = []

  kode ini menggunakan dictionary untuk menyimpan akun yang boleh login ke sistem, jadi role admin dan user dapat login ke sistem jika password benar,      jika salah akan diarahkan untuk input ulang maksimal 3 kali. lalu ada list kosong untuk menyimpan data peserta yang dimasukkan oleh admin.

C. Penggunaan fungsi login (line 12-16 python)
  def login(username, password):
    if username in akun and akun[username]["password"] == password:
        return True
    else:
        return False

  digunakan untuk memeriksa apakah username dan password yang dimasukkan benar     (login berhasil) atau salah (login gagal).

D. Penggunaan fungsi input skor (line 18-27 python)
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
      kode ini digunakan untuk memasukkan dan memvalidasi skor agar hanya menerima angka 0-100. jika melebihi atau kurang maka user akan diarahkan untuk menginput ulang.

E. Penggunaan fungsi dan library math untuk menghitung rata rata (line 29-32 python)
      def hitung_rata_rata(push_up, sit_up, lari):
      total = math.fsum([push_up, sit_up, lari])
      rata_rata = total / 3
      return rata_rata
      math.fsum digunakan untuk menjumlahkan ketiga skor lalu jumlah skor dibagi 3 untuk menghitung rata rata. Return digunakan untuk mengembalikan hasil rata rata agar bisa digunakan dibagian kode lainnya.

F. Penggunaan fungsi untuk kategori (line 34-42 python)
      def tentukan_kategori(rata_rata):
        if rata_rata <= 59:
            return "kurang"
        elif 60 <= rata_rata <= 75:
            return "cukup"
        elif 75 <= rata_rata <= 85:
            return "baik"
        else:
            return "sangat baik"
      Kode ini menggunakan fungsi untuk menentukan kategori tingkat kebugaran berdasarkan nilai rata-rata
      jika <= 59 masuk kategori kurang
      jika 60-75 masuk kategori cukup
      jika 76-85 masuk kategori baik
      jika >85 masuk kategori sangat baik

G. Pengunaan fungsi untuk menambah data (line 44-60 python)
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
    kode ini untuk dapat memasukkan data peserta, skor latihan, hasil rata-rat, menentukan kategori lalu menyimpan data ke data           peserta, Berikut ini outputnya
    <img width="667" height="420" alt="WhatsApp Image 2026-10-06 at 18 24 52" src="https://github.com/user-attachments/assets/b0d49a6b-14ce-4c4a-8867-ae71b19c4227" />

H. Penggunaan fungsi untuk hapus data (line 62-78 python)
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
      kode ini digunakan untuk menghapus data, jika admin belum memasukkan data maka output akan menghasilkan data belum dimasukkan. indeks digunakan untuk menampilkan no peserta dari 1 dan menggunakan pop untuk menghapus data.
berikut ini output programnya:
      <img width="1473" height="286" alt="WhatsApp Image 2026-10-06 at 18 27 22" src="https://github.com/user-attachments/assets/919e87ae-4c35-475e-b371-e13ecefd4474" />

I. Pengunaan fungsi untuk melihat data (line 80-91 python)
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
      kode ini digunakan untuk mengecek apakah data tersedia jika tidak output akan menampilkan data belum dimasukkan, jika data sudah ada maka program akan menampilkan data yang sudah dipanggil di kode ini yang berisikan nama, 3 skor, rata-rata skor,            kategori. 
berikut ini output dari program
      <img width="385" height="385" alt="WhatsApp Image 2026-10-06 at 18 25 23" src="https://github.com/user-attachments/assets/cd3bab00-e6d3-4b74-bafb-78e87aae9af6" />

J. Penggunaan fungsi untuk ubah data (line 93-130 python)
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
      Kode ini digunakan untuk memilih peserta yang akan dihapus berdasarkan nomor atau indeks, admin akan menginput ulang nama dan   skor peserta kemudian program akan menghitung ulang rata rata dan menyesuaikan kategori. Dan jika data belum dimasukkan maka output akan menampilkan data belum dimasukkan dan program akan meminta untuk mengisi (bagi admin)
berikut ini tampilan output di program
      <img width="1479" height="393" alt="WhatsApp Image 2026-10-06 at 18 27 08" src="https://github.com/user-attachments/assets/e3319afa-7774-4fa0-9095-a988303257ea" />

K. Penggunaan library os dan pwinput (line 132-150 python)
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
        Kode ini digunakan untuk menjalankan proses login dengan pwinput unutk menyembunyikan password dan menghitung karakter password, merapikan output, membatasi penggunaan login maksimal 3 kali.

L. Penggunaan kode untuk tampilan menu admin (line 152-176 python)
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
        Kode ini berfungsi untuk menampilkan menu utama pada admin yang berisikan 5 pilihan menu lalu menggunakan time 5 detik untuk menampilkan output terima kasih kepada admin sebelum program kembali ke halaman login.
        <img width="666" height="255" alt="WhatsApp Image 2026-10-06 at 18 27 39" src="https://github.com/user-attachments/assets/4cea8b0f-1bde-47a5-a2ce-68dd2c8a225c" />
    M. Penggunaan kode untuk tampilan menu user biasa (line 178-193 python)
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
        Kode ini berfungsi untuk menampilkan menu utama pada user yang berisikan 2 pilihan menu lalu menggunakan time selama 5 detik untuk menampilkan output terima kasih kepada admin sebelum program kembali ke halaman login
Berikut ini tampilan menu USER
        Pilihan no 1: <img width="471" height="129" alt="WhatsApp Image 2026-10-06 at 18 29 13" src="https://github.com/user-attachments/assets/a700ac4a-fab7-47f7-9096-32e87dd98673" />
        pilihan no 2: <img width="595" height="162" alt="WhatsApp Image 2026-10-06 at 18 29 25" src="https://github.com/user-attachments/assets/9c270441-bf51-4472-8088-86840a223999" />

PENGIMPLEMENTASIAN UNTUK NILAI TAMBAH (line 18-27 dan line 1-4 python)
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
Di kode ini pada bagian input skor, digunakan try-except untuk menangani kesalahan ketika pengguna memasukkan data yang bukan angka, serta validasi rentang nilai dari 0–100. Selain itu, terdapat pembatasan percobaan login maksimal 3 kali dan validasi pada pilihan menu. 

import pwinput
import os
import math
import time
Di kode ini menggunakan 4 library untuk password, membersihkan layar, menghitung rata rata, jeda 5 detik (penjelasan lebih lengkap ada di penjelasan program diatas)
