#test.py

from utility import *
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

while True:
    option = get_menu_option()
    match option:
        case "1": # Deposit
            account_type = get_account_type()
            new_balance = deposit_funds(account_type)
            update_account_balance(account_type, new_balance)
        case "2": # Withdraw
            account_type = get_account_type()
            new_balance = withdraw_funds(account_type)
            update_account_balance(account_type, new_balance)
        case "3": # Check Balance
            account_type = get_account_type()
            display_account_balance(account_type)
        case "4": # Transfer
            account_type_from = get_account_type()
            account_type_to = get_account_type()
            new_balance_from = transfer_funds(account_type_from, account_type_to)
            update_account_balance(account_type_from, new_balance_from)
        case "5": # Exit
            print("Thank You. Have A Great Day! ")
            break