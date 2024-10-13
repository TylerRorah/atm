from utility import *

while True:
  option = get_menu_option()
  match option:
    case 1: # Deposit
      print ("Deposit: Which Account?")
      account_type = get_account_type()
      new_balance = deposit_funds(account_type)
    
    case 2: # Withdraw
      print("Withdraw: Which Account? ")
      account_type = get_account_type()
      new_balance = withdraw_funds(account_type)
      
    case 3: #Check Balance
      print("Check Balance: Which Account?")
      account_type = get_account_type()
      balance = get_balance(account_type)
      print(f"Current balance in {account_type} is ${balance}.")

    case 4: # Transfer
        transfer_funds()

    case 5: #Exit
      print ("Thank You. Have A Great Day! ")
      break
