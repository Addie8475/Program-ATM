# Program ATM

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
