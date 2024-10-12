#atm user interface code here

import tkinter as tk
from atm import load_account_balances, get_current_account_balances, update_account_balance

class ATMUI:
    def __init__(self, root):
        self.root = root
        self.load_account_balances = load_account_balances
        self.get_current_account_balances = get_current_account_balances
        self.update_account_balance = update_account_balance
        self.checkings_account, self.savings_account = self.get_current_account_balances()
        self.account_type = "checking"
        self.entry_field = tk.Entry(self.root, width=20, font=("Arial", 20))
        self.entry_field.grid(row=0, column=0, columnspan=3)
        self.create_number_pad()
        self.create_atm_buttons()
        self.update_balance_labels()
        self.create_text_label()

    def create_text_label(self):
        self.text_label = tk.Label(self.root, text="", wraplength=200)
        self.text_label.grid(row=9, column=0, columnspan=5)

    def get_current_account_balances(self):
        return self.load_account_balances()['checkings_account'], self.load_account_balances()['savings_account']

    def deposit_funds(self, account_type: str) -> int:
        """Deposit funds into an account."""
        while True:
            try:
                deposit_amount = int(self.entry_field.get())
                if 1 <= deposit_amount <= 5000:
                    new_balance = self.get_current_account_balances()[account_type == "checking"]
                    new_balance += deposit_amount
                    self.text_label['text'] = f"New balance is ${new_balance}."
                    self.update_account_balance(account_type, new_balance)
                    return new_balance
                else:
                    self.text_label['text'] = "Deposit amount must be a valid integer between $1 and $5000"
            except ValueError:
                self.text_label['text'] = "Invalid input. Please enter a valid number."

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
        tk.Button(self.root, text="Deposit", command=lambda: self.deposit_funds(self.account_type)).grid(row=5, column=0)
        tk.Button(self.root, text="Withdraw", command=lambda: self.withdraw_funds(self.account_type)).grid(row=5, column=1)
        tk.Button(self.root, text="Check Balance", command=self.check_balance).grid(row=5, column=2)
        tk.Button(self.root, text="Switch Account", command=self.switch_account).grid(row=6, column=0, columnspan=3)
    
        self.entry_field = tk.Entry(self.root)
        self.entry_field.grid(row=7, column=0, columnspan=2)
    
        tk.Button(self.root, text="Submit", command=self.submit_amount).grid(row=7, column=2)
    
    def submit_amount(self):
        """Submit the deposit or withdrawal amount."""
        try:
            amount = int(self.entry_field.get())
            if self.withdraw_button.config('text')[-1] == "Withdraw":
                self.withdraw_funds(self.account_type, amount)
            else:
                self.deposit_funds(self.account_type, amount)
        except ValueError:
            self.text_label['text'] = "Invalid input. Please enter a valid number."

    def append_to_entry_field(self, value):
        self.entry_field.insert(tk.END, value)

    def withdraw_funds(self, account_type: str) -> int:
        """Withdraw funds from an account."""
        while True:
            try:
                withdraw_amount = int(self.entry_field.get())
                if 1 <= withdraw_amount <= 5000:
                    new_balance = self.get_current_account_balances()[account_type == "checking"]
                    if new_balance >= withdraw_amount:
                        new_balance -= withdraw_amount
                        self.text_label['text'] = f"New balance is ${new_balance}."
                        self.update_account_balance(account_type, new_balance)
                        return new_balance
                    else:
                        self.text_label['text'] = "Insufficient funds."
                else:
                    self.text_label['text'] = "Withdrawal amount must be a valid integer between $1 and $5000"
            except ValueError:
                self.text_label['text'] = "Invalid input. Please enter a valid number."

    def check_balance(self):
        print(f"Current balance is ${self.get_current_account_balances()[self.account_type == 'checking']}")

    def switch_account(self):
        if self.account_type == "checking":
            self.account_type = "savings"
        else:
            self.account_type = "checking"
        self.update_balance_labels()

    def update_balance_labels(self):
        self.checkings_balance_label = tk.Label(self.root, text=f"Checking balance: ${self.checkings_account}")
        self.checkings_balance_label.grid(row=7, column=0)
        self.savings_balance_label = tk.Label(self.root, text=f"Savings balance: ${self.savings_account}")
        self.savings_balance_label.grid(row=7, column=1)

if __name__ == "__main__":
    print("Creating GUI...")
    root = tk.Tk()
    atm_ui = ATMUI(root)
    print("GUI created. Starting main loop...")
    root.mainloop()
    print("Main loop exited.")