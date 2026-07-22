# day04/main.py

class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self.__balance = balance   # private balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print('Deposit must be positive.')
            return

        self.__balance += amount
        print(f'Deposited {amount} ETB')

    def withdraw(self, amount):
        if amount <= 0:
            print('Withdrawal must be positive.')
            return

        if amount > self.__balance:
            print('Insufficient balance.')
            return

        self.__balance -= amount
        print(f'Withdrew {amount} ETB')

    def statement(self):
        print(f'{self.owner} ({self.account_number}) - Balance: {self.balance} ETB')


# Test
acc1 = Account('Almaz', 'CBE-1001', 5000)
acc2 = Account('Hamere', 'CBE-1002', 3000)

acc1.deposit(1000)
acc1.withdraw(700)

acc2.withdraw(5000)   # should fail

acc1.statement()
acc2.statement()