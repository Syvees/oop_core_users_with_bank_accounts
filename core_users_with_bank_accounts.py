class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate=0.02, balance=0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance (self):
        y=self.account.display_account_info()
        return self

class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = balance
        self.int_rate = int_rate

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            self.balance -= 5  
            print("Insufficient funds: Charging a $5 fee")
        return self
    
    def display_account_info (self):
        print(f"Balance: {self.balance}")
        return self

harry = User ("Harry Potter", "harry.potter@gmail.com")
harry.make_deposit(123).make_withdraw(70).display_user_balance()

print(harry.account.balance)