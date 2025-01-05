# Program ATM

**Kode Python**

![Screenshot_106](https://github.com/user-attachments/assets/a521bb3b-f6e1-466d-9653-53486bf1b04b)
![Screenshot_107](https://github.com/user-attachments/assets/7e8ff9d0-b41e-49f5-8b4f-dc3f09b89142)
![Screenshot_108](https://github.com/user-attachments/assets/de7b880d-1617-4874-a7f9-20d1cba7bec3)
![Screenshot_109](https://github.com/user-attachments/assets/f58892a9-b995-40ae-b611-d4a147010568)
![Screenshot_110](https://github.com/user-attachments/assets/d36a77ea-59ab-4efb-8dd3-90f5c74acf4f)

**Input dan Output**

![Screenshot_111](https://github.com/user-attachments/assets/98b04ec6-c5d0-4a1e-8dff-b092cb7bace0)
![Screenshot_112](https://github.com/user-attachments/assets/fd418946-b2ad-4d6b-a926-a8d27e21e0b6)

 # 1. Struktur Program

Program dibagi menjadi beberapa modul (folder dan file) untuk menjaga keteraturan, memudahkan pengelolaan, dan memungkinkan pengembangan lebih lanjut.

•	Folder data: Mengelola data akun, seperti PIN, saldo, dan transaksi. Penyimpanan data dilakukan menggunakan file JSON.

•	Folder view: Menangani tampilan antarmuka ke pengguna, seperti menampilkan menu, meminta input, dan memberikan output.

•	File main.py: Bertindak sebagai kontrol utama, menghubungkan logika dalam data dan view, serta mengatur jalannya program.

# 2. Penjelasan Tiap File

**a. data/database.py**

File ini mengelola logika data dengan menggunakan file JSON sebagai penyimpanan. Fungsi-fungsinya meliputi:

•	os: Digunakan untuk menangani path file secara dinamis, sehingga program bisa berjalan di berbagai sistem operasi tanpa masalah.

•	json: Modul untuk bekerja dengan data JSON, seperti membaca (parsing) dan menyimpan (serialisasi) data dalam format file JSON.

•	os.path.dirname(__file__): Mengembalikan lokasi folder tempat file database.py berada (dalam hal ini, folder data).

•	os.path.join(...): Menggabungkan path folder data dengan nama file accounts.json, sehingga path file menjadi relatif ke lokasi folder data.

•	load_accounts: Membaca file JSON dan mengembalikan data akun dalam bentuk dictionary.

•	save_accounts: Menyimpan data akun ke file JSON.

•	validate_account: Memeriksa apakah nomor akun dan PIN yang dimasukkan sesuai dengan data di file JSON.

•	update_balance: Memperbarui saldo akun berdasarkan transaksi setor tunai atau tarik tunai.

**b. view/interface.py**

File ini menangani antarmuka pengguna (User Interface). Fungsi-fungsinya meliputi:

•	show_menu: Menampilkan daftar menu ATM (cek saldo, setor tunai, tarik tunai, keluar).

•	show_balance: Menampilkan saldo akun pengguna.

•	ask_account_details: Meminta input nomor akun dan PIN.

•	ask_transaction_amount: Meminta input jumlah uang yang akan ditransaksikan.

•	show_message: Menampilkan pesan umum ke pengguna (seperti notifikasi sukses atau kesalahan).

**c. main.py**

File ini adalah inti dari program, mengelola alur eksekusi dengan langkah-langkah berikut:

1.	Login: Meminta nomor akun dan PIN, lalu memvalidasi data.

2.	Menu Utama:

o	Cek Saldo: Menampilkan saldo pengguna.

o	Setor Tunai: Meminta jumlah setor tunai, menambah saldo, dan menyimpannya.

o	Tarik Tunai: Memeriksa jumlah tarik tunai apakah mencukupi saldo, lalu menguranginya jika valid.

o	Keluar: Mengakhiri program.

3.	Pengolahan Data: Menggunakan fungsi dari data/database.py untuk memproses transaksi dan mengupdate saldo.

4.	Tampilan: Memanfaatkan fungsi dari view/interface.py untuk menampilkan pesan atau meminta input dari pengguna.
