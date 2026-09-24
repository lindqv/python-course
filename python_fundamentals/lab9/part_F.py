class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account with balance {self.balance} and owner {self.owner}"

class SavingsAccount(Account):
    def __init__(self, owner, balance, interest_rate):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def __str__(self):
        return f"Savings account with balance {self.balance}, interest rate {self.interest_rate} and owner {self.owner}"

account = Account("Ada", 3000)
savings_account = SavingsAccount("Ada", 10000, 2.5)

print(account)
print(savings_account)