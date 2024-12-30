import os
import json

DATABASE_FILE = os.path.join(os.path.dirname(__file__), "accounts.json")

def load_accounts():
    try:
        with open(DATABASE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_accounts(accounts):
    with open(DATABASE_FILE, "w") as file:
        json.dump(accounts, file)

def validate_account(account_number, pin):
    accounts = load_accounts()
    if account_number in accounts and accounts[account_number]["pin"] == pin:
        return accounts[account_number]
    return None

def update_balance(account_number, amount):
    accounts = load_accounts()
    if account_number in accounts:
        accounts[account_number]["balance"] += amount
        save_accounts(accounts)
        return accounts[account_number]["balance"]
    return None
