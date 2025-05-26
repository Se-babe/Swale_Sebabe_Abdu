# Real-World Bank System using OOP

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Deposited {amount}, new balance: {self.balance}')

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'Withdrew {amount}, new balance: {self.balance}')
        else:
            print('Insufficient funds')

    def display_balance(self):
        print(f'Account {self.account_number} balance: {self.balance}')


# Subclass: SavingAccount
class SavingAccount(BankAccount):
    def __init__(self, account_number, balance, interest_rate):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.balance * self.interest_rate / 100
        self.balance += interest
        print(f'Interest of {interest} added. New balance: {self.balance}')


# Subclass: CurrentAccount
class CurrentAccount(BankAccount):
    def __init__(self, account_number, balance, overdraft_limit):
        super().__init__(account_number, balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f'Withdrew {amount}. New balance: {self.balance}')
        else:
            print('Exceeded the overdraft limit')


# Creating objects
saving = SavingAccount('SAO5555', 100000, 5)
current = CurrentAccount('CURE3333', 50000, 10000)

# Test SavingAccount
print("💰 Saving Account:")
saving.display_balance()
saving.add_interest()
saving.withdraw(20000)

print("\n🏦 Current Account:")
# Test CurrentAccount
current.display_balance()
current.withdraw(70000)
current.withdraw(45000)  # Should exceed overdraft
