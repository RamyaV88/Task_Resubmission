# Problem 1 - Bank Account
# Created a base class BankAccount with few attributes

class BankAccount: 
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

# Created a method deposit within the base class
    def deposit(self, amount): 
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: ${self.balance}")
        else:
            print("Invalid deposit amount.")

# Created a method withdraw within the base class
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

# Created a method get balance within the base class to return the balance amount
    def get_balance(self): 
        return self.balance
    
# Created a method get account info within the base class to return the account information
    def get_account_info(self):
      return f"Account Number: {self.account_number}\nAccount Holder: {self.account_holder_name}\nBalance: ${self.balance}"
    
# Created a derived class SavingsAccount which inherits the base class BankAccount
class SavingsAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, interest_rate, interest_earned):
        super().__init__(account_number, account_holder_name, balance)
        self.interest_rate = interest_rate
        self.interest_earned = interest_earned
# Created a method to calculate interest
    def calculate_interest(self, time_period):
        interest = self.balance * self.interest_rate * time_period
        self.interest_earned += interest
        return f"Interest earned over {time_period} years: ${interest}. Total interest earned: ${self.interest_earned}"

# Created a derived class CurrentAccount which inherits the base class BankAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_number, account_holder_name, balance, overdraft_limit=1000):
        super().__init__(account_number, account_holder_name)
        self.overdraft_limit = overdraft_limit

# Overriding the withdraw method to include overdraft limit
    def withdraw(self, amount): 
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount}. New balance: ${self.balance}")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

# Created an object of the class BankAccount
account1 = BankAccount("5455126458", "Mr. Alex Jane", 5000) 
print(account1.get_account_info())
print()
# Passing the amount to deposit and withdraw
account1.deposit(1000) 
account1.withdraw(500) 
print()
# Printing the account details with the balance amount
print(account1.get_account_info()) 
print()
# Created an object of the class SavingsAccount
account2 = SavingsAccount("5455126458", "Mr. Alex Jane", 5000, 0.5, 0) 
print(account2.calculate_interest(0.5))
print()
account3 = CurrentAccount("5455178450","Mr. Joseph Jai", 5000, 1000)
print(account3.get_account_info())
account3.withdraw(1200) 
