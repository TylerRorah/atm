#stored functions for use in other programs
import json
def deposit_funds(account_type: str) -> int:
    """Deposit funds into an account."""
    while True:
        deposit_amount = handle_invalid_input("How much would you like to deposit? $")
        if deposit_amount <= 0:
            print("Invalid input. Please enter a positive number.")
        elif deposit_amount > 5000:
            print("Deposit amount exceeds the limit of $5000. Please enter a valid amount.")
        else:
            new_balance = get_balance(account_type) + deposit_amount
            print(f"New balance is ${new_balance}.")
            update_account_balance(account_type, new_balance)
            return new_balance
            
def withdraw_funds(account_type: str) -> int:
    withdrawal_amount = handle_invalid_input("How much would you like to withdraw? $")
    balance = get_balance(account_type)
    if balance == 0:
        print("Insufficient funds.")
    elif 0 < withdrawal_amount <= balance:
        new_balance = balance - withdrawal_amount
        print(f"New balance is ${new_balance}.")
        update_account_balance(account_type, new_balance)
        return new_balance
    else:
        print("Invalid withdrawal amount. Please try again.")
        

def get_menu_option():
    menu_options = {
        "1": "Deposit",
        "2": "Withdraw",
        "3": "Check Balance",
        "4": "Transfer",
        "5": "Exit"
    }
    while True:
        for option, description in menu_options.items():
            print(f"{option}. {description}")
        choice = input("Enter a number (1-5): ")
        if choice in menu_options:
            return choice
        else:
            print("Invalid choice. Please try again.")
def get_account_type():
    account_types = {
        "1": "checking",
        "2": "savings"
    }
    while True:
        print("1. Checking")
        print("2. Savings")
        choice = input("Enter 1 or 2: ")
        if choice in account_types:
            return account_types[choice]
        else:
            print("Invalid choice. Please try again.")

def transfer_funds(account_type_from, account_type_to):
    balances = get_current_account_balances()
    if account_type_from == "Checking":
        balance_from = balances[0]
    else:
        balance_from = balances[1]
    if account_type_to == "Checking":
        balance_to = balances[0]
    else:
        balance_to = balances[1]
    while True:
        try:
            transfer_amount = int(input("How much would you like to Transfer? $"))
            if 0 < transfer_amount <= balance_from:
                new_balance_from = balance_from - transfer_amount
                new_balance_to = balance_to + transfer_amount
                print(f"Transfer successful. New balance in {account_type_from} is ${new_balance_from}. New balance in {account_type_to} is ${new_balance_to}.")
                return new_balance_from, new_balance_to
            else:
                print("Invalid transfer amount. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def update_account_balance(account_type, new_balance):
    global checkings_account, savings_account
    if account_type == "checking":
        checkings_account = new_balance
    elif account_type == "savings":
        savings_account = new_balance
    save_account_balances(checkings_account, savings_account)
    try:
        account_balance = load_account_balances()
        checkings_account = account_balance['checkings_account']
        savings_account = account_balance['savings_account']
    except Exception as e:
        print(f"Failed to load account balances: {e}")

def save_account_balances(checkings_account, savings_account):
    try:
        with open('account_balances.json', 'w') as f:
            json.dump({'checkings_account': checkings_account, 'savings_account': savings_account}, f)
    except Exception as e:
        print(f"Error saving account balances: {e}")

def load_account_balances() -> dict:
    try:
        with open("account_balances.json", "r") as file:
            account_balance = json.load(file)
            if "checkings_account" not in account_balance or "savings_account" not in account_balance:
                raise ValueError("Invalid account balance")
            return account_balance
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Error loading account balances: {e}")
        return {"checkings_account": 0, "savings_account": 0}

def get_balance(account_type):
    if account_type == "checking":
        return checkings_account if checkings_account is not None else 0
    elif account_type == "savings":
        return savings_account if savings_account is not None else 0

def get_current_account_balances():
    try:
        account_balance = load_account_balances()
        return account_balance['checkings_account'], account_balance['savings_account']
    except Exception as e:
        print(f"Failed to load account balances: {e}")
        return 0, 0

def display_account_balance(account_type):
    balance = get_balance(account_type)
    print(f"Current balance in {account_type} is ${balance}.")
def handle_invalid_input(prompt):
    while True:
        try:
            num = int(input(prompt))
            if num <= 0:
                print("Invalid input. Please enter a positive number.")
            else:
                return num
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Usage:
checkings_account, savings_account = get_current_account_balances()