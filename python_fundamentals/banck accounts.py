class BankAccount:

    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount	# the specific user's account increases by the amount of the value received
    def withdrawal(self, amount):
        self.balance -= amount 
    def display_user_info(self):
        print(f"Balance: {self.balance}")
   
    def yield_interest(self): 
        self.balance += self.int_rate * self.balance


moha = BankAccount(10,100)
moha.deposit(100)
moha.display_user_info()




