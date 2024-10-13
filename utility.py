#stored functions for use in other programs
import json
def deposit_funds(account_type: str) -> int:
    """Deposit funds into an account."""
    deposit_amount = handle_invalid_input("How much would you like to deposit? $")
    if 1 <= deposit_amount <= 5000:
        new_balance = get_balance(account_type) + deposit_amount
        print(f"New balance is ${new_balance}.")
        update_account_balance(account_type, new_balance)
        return new_balance  # Return the new balance
            
def withdraw_funds(account_type: str) -> int: 
    withdrawal_amount = handle_invalid_input("How much would you like to withdraw? $")
    if 0 < withdrawal_amount <= get_balance(account_type):
        new_balance = get_balance(account_type) - withdrawal_amount
        print(f"New balance is ${new_balance}.")
        update_account_balance(account_type, new_balance)
        return new_balance  # Return the new balance
        

def get_menu_option() -> int:
    """
    Displays menu options and returns the user's selection as an integer.
    """
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transfer")
        print("5. Exit")
        try:
            option = int(input("Enter a number (1-5): "))
            if 1 <= option <= 5:
                return option
            else:
                print("Invalid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
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
    print("Transfer from: Which Account?")
    account_type_from = get_account_type()
    print("Transfer to: Which Account?")
    account_type_to = get_account_type()
    if account_type_from != account_type_to:
        transfer_amount = handle_invalid_input("How much would you like to Transfer? $")
        if 0 < transfer_amount <= get_balance(account_type_from):
            new_balance_from = get_balance(account_type_from) - transfer_amount
            new_balance_to = get_balance(account_type_to) + transfer_amount
            update_account_balance(account_type_from, new_balance_from)
            update_account_balance(account_type_to, new_balance_to)
            print(f"Transfer successful. New balance in {account_type_from} is ${new_balance_from}. New balance in {account_type_to} is ${new_balance_to}.")
    else:
        print("Cannot transfer to the same account. Please try again.")
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
        return checkings_account
    elif account_type == "savings":
        return savings_account

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
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Usage:
checkings_account, savings_account = get_current_account_balances()