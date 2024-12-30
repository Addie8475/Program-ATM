def show_menu():
    print("\n=== ATM Menu ===")
    print("1. Cek Saldo")
    print("2. Setor Tunai")
    print("3. Tarik Tunai")
    print("4. Keluar")

def show_balance(balance):
    print(f"\nSaldo Anda: Rp {balance}")

def ask_account_details():
    account_number = input("Masukkan nomor akun: ")
    pin = input("Masukkan PIN: ")
    return account_number, pin

def ask_transaction_amount():
    return int(input("Masukkan jumlah transaksi: "))

def show_message(message):
    print(f"\n{message}")
