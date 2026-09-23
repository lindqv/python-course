class Account:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, owner: str, balance: float, interest_rate: float):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

account = Account("Ada", 5000)
savings = SavingsAccount("Ada", 20000, 2.5)

print(account.owner, account.balance)
print(savings.owner, savings.balance, savings.interest_rate)

# "is-a" statement
# SavingsAccount is an Account. 
# Therefore the inheritance makes sense.