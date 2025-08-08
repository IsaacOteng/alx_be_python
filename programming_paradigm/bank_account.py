class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        account_balance = 0

    def deposit(self, amount):
        account_balance = self.account_balance + amount
    
    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False
    
    def display_balance(self):
        print(f"Current balance: ${self.account_balance}")


acc = BankAccount(1000)
acc.display_balance()