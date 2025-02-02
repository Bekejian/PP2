class BankAccount:
    def _init_(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit {amount}. New balance: {self.balance}")

    def withdraw(self, amount):    
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawal {amount}. New balance: {self.balance}")

acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
acc.withdraw(200)