#test.py

from utility import *

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
            print("Transfer: Which Account?")
            account_type_from = get_account_type()
            print("Transfer to: Which Account?")
            account_type_to = get_account_type()
            new_balance_from, new_balance_to = transfer_funds(account_type_from, account_type_to)
            update_account_balance(account_type_from, new_balance_from)
            update_account_balance(account_type_to, new_balance_to)
        case "5": # Exit
            print("Thank You. Have A Great Day! ")
            break