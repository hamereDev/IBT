# day07/main.py

class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.balance = balance
        self.history = []   # stack

    def deposit(self, amount):
        self.balance += amount
        self.history.append(('deposit', amount))

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(('withdraw', amount))
        else:
            print('Insufficient balance.')

    def undo_last(self):
        if not self.history:
            print('No transaction to undo.')
            return

        tx_type, amount = self.history.pop()

        if tx_type == 'deposit':
            self.balance -= amount
        else:
            self.balance += amount

    def statement(self):
        print(f'{self.owner} ({self.account_number}) - Balance: {self.balance} ETB')


class AccountRegistry:
    def __init__(self):
        self.by_number = {}   # O(1) lookup
        self.order = []

    def add(self, account):
        self.by_number[account.account_number] = account
        self.order.append(account.account_number)

    def find(self, number):
        return self.by_number.get(number)

    def list_all(self):
        accounts = []

        for number in self.order:
            accounts.append(self.by_number[number])

        return accounts


# Test
registry = AccountRegistry()

a1 = Account('Almaz', 'CBE-1001', 5000)
a2 = Account('Hamere', 'CBE-1002', 3000)

registry.add(a1)
registry.add(a2)

# O(1) lookup
found = registry.find('CBE-1002')

print('Lookup result:')
found.statement()

# Ordered listing
print('\\nAll accounts:')

for acc in registry.list_all():
    acc.statement()

# Transaction history stack
a1.deposit(1000)
a1.withdraw(500)

print('\\nBefore undo:', a1.balance)

a1.undo_last()
print('After first undo:', a1.balance)

a1.undo_last()
print('After second undo:', a1.balance)