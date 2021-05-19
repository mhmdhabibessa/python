class BankAccount:
    def __init__(self,rate,balance):
        self.balance=balance
        self.rate=rate
    def deposit(self,amount):
        self.balance+=amount
        return self
    def withdraw(self,amount):
        self.balance-=amount
        return self
    def display(self):
        print(self.balance)
    def yield_interest(self):
        self.balance=self.balance+(self.rate*self.balance)
        return self
mhmd=BankAccount(0.5,1000)
habib=BankAccount(0.1,1000)
mhmd.deposit(50)
mhmd.deposit(70)
mhmd.withdraw(120)
mhmd.display()
habib.deposit(50).deposit(50).deposit(50).withdraw(50).yield_interest().display()