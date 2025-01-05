from data.database import validate_account, update_balance
from view.interface import show_menu, show_balance, ask_account_details, ask_transaction_amount, show_message

def main():
    print("=== Selamat Datang di ATM ===")
    
    account = None
    while account is None:
        account_number, pin = ask_account_details()
        account = validate_account(account_number, pin)
        if not account:
            show_message("Nomor akun atau PIN salah. Silakan coba lagi.")
    
    # Jika login berhasil
    while True:
        show_menu()
        choice = input("Pilih menu: ")
        
        if choice == "1":
            show_balance(account["balance"])
        
        elif choice == "2":
            amount = ask_transaction_amount()
            if amount > 0:
                new_balance = update_balance(account_number, amount)
                account["balance"] = new_balance  # Update saldo dalam memori
                show_balance(new_balance)
            else:
                show_message("Jumlah harus positif.")
        
        elif choice == "3":
            amount = ask_transaction_amount()
            if 0 < amount <= account["balance"]:
                new_balance = update_balance(account_number, -amount)
                account["balance"] = new_balance  # Update saldo dalam memori
                show_balance(new_balance)
            else:
                show_message("Jumlah tidak valid atau saldo tidak mencukupi.")
        
        elif choice == "4":
            show_message("Terima kasih telah menggunakan ATM!")
            break
        
        else:
            show_message("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
