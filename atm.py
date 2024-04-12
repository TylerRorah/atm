#With this personal project I created an ATM program that presents you a mulitude of functions you would find at an actual machine. 

#functionality that i would like to add
  # set a limit to amount an individual can deposit through 1 transaction
  # set current balance of checking/savings up to change variable value after user input each time program runs it needs to be based off transaction history. 
 # keep menu popping up after any action by user. Thinking of doing a Class or while loop

 
def which_account() -> int:
  #ask for user input then loop through until there is a valid entry
  while True:
    print ("1 = Checkings")
    print ("2 = Savings")
    try:
      output = int(input("Enter a Number 1 or 2: "))
      if output == 1 or output == 2:
        return output
      else:
        print("Please Try Again. ")
    except ValueError:
      print("Invalid input. Please enter a valid number. ")

  
def choice_for_change():
  choice = which_account() 
  if choice == 1:
    output = checkings_account
  elif choice == 2:
    output = savings_account 
  return output 

def menu() -> int:
  # display menu options and check for input error
  while True:
    print ("1 = Deposit")
    print ("2 = Withdrawl")
    print ("3 = Check Balance")
    print ("4 = Transfer")
    print ("5 = Exit")
    try:
      option = int(input("Enter a Number (1:5): " ))
      if option >= 1 and option <= 5:
        return option
      else:
        print("Please Try Again. ")
    except ValueError:
      print("Invalid input. Please enter a number. ")
  
checkings_account = 1000
savings_account = 3000

while True:

  option = menu()

  match option:
    case 1: # Deposit
      print ("Deposit: Which Account?")
      output = choice_for_change() 
      
      def deposit_funds(output) -> int: # passes output through the deposit funds function
        while True:
          try: 
            funds = int(input("How much would you like to deposit? $"))
            if 0 < funds > 5000: # set a maximum and minimum limit for deposit
              print ("Maximum Limit Per Transaction = $5000")
              print ("Minimum Limit Per Transaction = $1")
              print ("Please Try Again. ")
            else:
              current_balance = funds + output
              print (f"New Balance is ${current_balance}.")
              return current_balance
          except ValueError:
            print("Invalid input. Please enter a number. ")
         
      
      deposit_funds(output) # might be an issue
    
    case 2: # Withdrawl
      print("Withdrawl: Which Account? ")
      output = choice_for_change()

      def withdrawl_funds(output):
        funds = int(input("How much would you like to deposit? $"))
        current_balance = funds - output
        print (f"New Balance is {current_balance}.")
        return current_balance 
        
      withdrawl_funds(output)
    
    case 3: # Check Balance
      output = which_account()
      if output == 1:
        print(checkings_account)
      elif output == 2:
        print(savings_account)

    case 4: # Transfer
      print ("You chose transfer. ")
      while True:
        print ("Please choose which account. ")
        which_account() # have user choose account 1 or 2 then assign that to output
        choice_for_change() # takes output and assigns it to checking or saving
        try:
          transfer_amount = int(input("How much would you like to Transfer? "))
          if 0 < transfer_amount <= choice_for_change():
            # do something with the valid transfer amount
            pass
          else:
            print("Invalid Transfer Amount. Please Try Again. ")
        except ValueError:
          print("Please enter a valid number for the transfer amount. ")

    case 5: #Exit
      print ("Thank You. Have A Great Day! ")
      break