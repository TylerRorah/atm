import json

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

#Load the initial account balances from the JSON file
try:
    account_balance = load_account_balances()
    checkings_account = account_balance['checkings_account']
    savings_account = account_balance['savings_account']
except Exception as e:
    print(f"Failed to load account balances: {e}")
    # Handle the error or exit the program
def get_balance(account_type):
    if account_type == "checking":
        return checkings_account
    elif account_type == "savings":
        return savings_account
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
  
def get_current_account_balances():
    try:
        account_balance = load_account_balances()
        return account_balance['checkings_account'], account_balance['savings_account']
    except Exception as e:
        print(f"Failed to load account balances: {e}")
        return 0, 0

# Usage:
checkings_account, savings_account = get_current_account_balances()
def deposit_funds(account_type: str) -> int:
        """Deposit funds into an account."""
        while True:
          try:
              deposit_amount = int(input("How much would you like to deposit? $"))
              if 1 <= deposit_amount <= 5000:
                  new_balance = get_balance(account_type) + deposit_amount
                  print(f"New balance is ${new_balance}.")
                  update_account_balance(account_type, new_balance)
                  return new_balance  # Return the new balance
              else:
                  print("Deposit amount must be a valid integer between $1 and $5000")
          except ValueError:
              print("Invalid input. Please enter a valid number.")
def withdraw_funds(account_type: str) -> int: 
         while True:
          try:
              withdrawal_amount = int(input("How much would you like to withdraw? $"))
              if 0 < withdrawal_amount <= get_balance(account_type):
                  new_balance = get_balance(account_type) - withdrawal_amount
                  print(f"New balance is ${new_balance}.")
                  update_account_balance(account_type, new_balance)
                  return new_balance  # Return the new balance
              else:
                  print("Invalid withdrawal amount. Please try again.")
          except ValueError:
              print("Invalid input. Please enter a valid number.")
def select_account() -> int:
    """Ask user to select an account and return their selection as an integer."""
    while True:
        print("1. Checking")
        print("2. Savings")
        try:
            selection = int(input("Enter 1 or 2: "))
            if selection in (1, 2):
                return selection
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def choice_for_change():
  choice = select_account()
  if choice == 1:
      return "checking"
  elif choice == 2:
      return "savings"
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
  

while True:
  option = get_menu_option()
  match option:
    case 1: # Deposit
      print ("Deposit: Which Account?")
      account_type = choice_for_change()
      new_balance = deposit_funds(account_type)
    
    case 2: # Withdraw
      print("Withdraw: Which Account? ")
      account_type = choice_for_change()
      new_balance = withdraw_funds(account_type)
      
    case 3: #Check Balance
      print("Check Balance: Which Account?")
      account_type = choice_for_change()
      balance = get_balance(account_type)
      print(f"Current balance in {account_type} is ${balance}.")

    case 4: # Transfer
      while True:
        print("Transfer: Which Account?")
        account_type_from = choice_for_change()
        print("Transfer to: Which Account?")
        account_type_to = choice_for_change()
        if account_type_from != account_type_to:
            transfer_amount = int(input("How much would you like to Transfer? $"))
            if 0 < transfer_amount <= get_balance(account_type_from):
                new_balance_from = get_balance(account_type_from) - transfer_amount
                new_balance_to = get_balance(account_type_to) + transfer_amount
                update_account_balance(account_type_from, new_balance_from)
                update_account_balance(account_type_to, new_balance_to)
                print(f"Transfer successful. New balance in {account_type_from} is ${new_balance_from}. New balance in {account_type_to} is ${new_balance_to}.")
            else:
                print("Invalid transfer amount. Please try again.")
        else:
            print("Cannot transfer to the same account. Please try again.")

    case 5: #Exit
      print ("Thank You. Have A Great Day! ")
      break
