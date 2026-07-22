

class Account:
    def __init__(self, owner, number, balance=0):
        self.owner = owner
        self.number = number
        self._balance = balance
        self.transactions = []

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.transactions.append(amount)

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.transactions.append(-amount)

    def __str__(self):
        return f'{self.number} | {self.owner} | Balance: {self.balance}'


class AccountRegistry:
    def __init__(self):
        self.by_number = {}

    def add_account(self, account):
        self.by_number[account.number] = account