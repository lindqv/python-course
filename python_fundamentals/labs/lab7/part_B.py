class Book:
    def __init__(self, title: str, author: str, pages: int = 0):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

books = [
    Book("Orlando", "Virginia Woolf", 350),
    Book("The Picture of Dorian Gray", "Oscar Wilde", 300),
    Book("Hamlet", "William Shakespeare", 200),
    Book("Frankenstein", "Mary Shelley", 250),
    ]

for book in books:
    print(book.is_long())


class BankAccount:
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            raise ValueError("Cannot withdraw more than is stored")
        else:
            self.balance -= amount
            return amount


class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed

    def complete(self):
        self.completed = True

    def reopen(self):
        self.completed = False


account1 = BankAccount("Ada", 1000)
account2 = BankAccount("Alan", 1001)

print(account1.balance, account2.balance)
amount = account2.withdraw(1)
print(account1.balance, account2.balance)
account1.deposit(amount)
print(account1.balance, account2.balance)