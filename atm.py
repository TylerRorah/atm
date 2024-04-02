#With this personal project I created an ATM program that presents you a mulitude of functions you would find at an actual machine. 

#functionality that i would like to add
  # set a limit to amount an individual can deposit through 1 transaction
  # set current balance of checking/savings up to change variable value after user input each time program runs it needs to be based of transaction history. 
 # keep menu popping up after any action by user. Thinking of doing a Class or while loop

def which_account():
  #ask for user input then loop through until there is a valid entry
  while True:
    print ("1 = Checkings")
    print ("2 = Savings")
    output = int(input("Enter a Number: "))
    if output == 1 or output == 2:
      return output
    else:
      print("Please Try Again. ")
  
def choice_for_change(): # this does not check for error and lets user put whatever
  choice = which_account() 
  if choice == 1:
    output = checkings_account
  elif choice == 2:
    output = savings_account 
  return output 

def menu():
  # display menu options and check for input error
  while True:
    print ("1 = Deposit")
    print ("2 = Withdrawl")
    print ("3 = Check Balance")
    print ("4 = Transfer")
    option = int(input("Enter a Number (1:4): " ))
    if option >= 1 and option <= 4:
      return option
    else:
      print("Please Try Again. ")
  
option = menu()
checkings_account = 1000
savings_account = 3000

match option:
  case 1: # Deposit
    print ("Deposit: Which Account?")
    output = choice_for_change() 
    
    def deposit_funds(output):
      funds = int(input("How much would you like to deposit? $"))
      current_balance = funds + output
      print (f"New Balance is ${current_balance}.")
      return current_balance 
      
    deposit_funds(output) # might be an issue
    menu() 
    
  case 2: # Withdrawl
    print("Withdrawl: Which Account? ")
    output = choice_for_change()

    def withdrawl_funds(output):
      funds = int(input("How much would you like to deposit? $"))
      current_balance = funds - output
      print (f"New Balance is {current_balance}.")
      return current_balance 
      
    withdrawl_funds(output)
    menu() 
    
  case 3: # Check Balance
    output = which_account()

    if output == 1:
      print(checkings_account)
    elif output == 2:
      print(savings_account)
    while output > 2: #unrealistic because you can't enter negative on keypad at ATM
      print("Not a Valid Entry")
      output = which_account()
      if output == 1:
        print(checkings_account)
      elif output == 2:
        print(savings_account)

    
    
  case 4: # Transfer
    print ("You chose transfer")
  case anything_else:
    print ("Please Try Again")