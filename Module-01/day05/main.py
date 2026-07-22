# day05/main.py

class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            print('Insufficient balance.')

    def statement(self):
        print(f'Account  {self.owner}  Balance: {self.balance} ETB')


class SavingsAccount(Account):
    def __init__(self, owner, account_number, balance=0, rate=0.05):
        super().__init__(owner, account_number, balance)
        self.rate = rate

    def add_interest(self):
        interest = self.balance * self.rate
        self.deposit(interest)

    def statement(self):
        print(f'Savings  {self.owner}  Balance: {self.balance:.2f} ETB')


class CurrentAccount(Account):
    def __init__(self, owner, account_number, balance=0, overdraft=1000):
        super().__init__(owner, account_number, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= self.balance + self.overdraft:
            self._balance -= amount
        else:
            print('Overdraft limit exceeded.')

    def statement(self):
        print(f'Current | {self.owner} | Balance: {self.balance:.2f} ETB')


# Test
a1 = SavingsAccount('Almaz', 'S-1001', 5000)
a2 = CurrentAccount('Hamere', 'C-2001', 2000, overdraft=1500)

a1.add_interest()
a2.withdraw(3000)

accounts = [a1, a2]

for acc in accounts:
    acc.statement()