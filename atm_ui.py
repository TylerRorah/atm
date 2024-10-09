#atm user interface code here

import tkinter as tk

print("Script is being executed...") #here for debugging purposes
class ATMUI:
    def __init__(self, root):
        self.root = root
        self.checkings_account, self.savings_account = self.get_current_account_balances()
        self.account_type = "checking"
        self.entry_field = tk.Entry(self.root, width=20, font=("Arial", 20))
        self.entry_field.grid(row=0, column=0, columnspan=3)
        self.create_number_pad()
        self.create_atm_buttons()
        self.update_balance_labels()

    def get_current_account_balances(self):
        # Load account balances from file or database
        # For example:
        self.checkings_account = 1000.0
        self.savings_account = 500.0
        return self.checkings_account, self.savings_account

    def deposit_funds(self, account_type, amount):
        # ATM logic code to deposit funds
        if account_type == "checking":
            self.checkings_account += amount
        elif account_type == "savings":
            self.savings_account += amount

    def create_number_pad(self):
        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '0'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.root, text=button, width=5, command=lambda button=button: self.append_to_entry_field(button)).grid(row=row_val, column=col_val)
            col_val += 1
            if col_val > 2:
                col_val = 0
                row_val += 1

    def create_atm_buttons(self):
        tk.Button(self.root, text="Deposit", command=self.deposit).grid(row=4, column=0)
        tk.Button(self.root, text="Withdraw", command=self.withdraw).grid(row=4, column=1)
        tk.Button(self.root, text="Check Balance", command=self.check_balance).grid(row=4, column=2)
        tk.Button(self.root, text="Switch Account", command=self.switch_account).grid(row=5, column=0, columnspan=3)

    def append_to_entry_field(self, value):
        self.entry_field.insert(tk.END, value)

    def deposit(self):
        try:
            amount = int(self.entry_field.get())
            new_balance = deposit_funds(self.account_type, amount)
            update_account_balance(self.account_type, new_balance)
            self.update_balance_labels()
            self.entry_field.delete(0, tk.END)
        except ValueError:
            print("Invalid amount")

    def withdraw(self):
        # implement withdraw functionality
        pass

    def check_balance(self):
        print(f"Current balance is ${get_balance(self.account_type)}")

    def switch_account(self):
        if self.account_type == "checking":
            self.account_type = "savings"
        else:
            self.account_type = "checking"
        self.update_balance_labels()

    def update_balance_labels(self):
        self.checkings_balance_label = tk.Label(self.root, text=f"Checking balance: ${self.checkings_account}")
        self.checkings_balance_label.grid(row=6, column=0)
        self.savings_balance_label = tk.Label(self.root, text=f"Savings balance: ${self.savings_account}")
        self.savings_balance_label.grid(row=6, column=1)

if __name__ == "__main__":
    print("Creating GUI...")
    root = tk.Tk()
    atm_ui = ATMUI(root)
    print("GUI created. Starting main loop...")
    root.mainloop()
    print("Main loop exited.")