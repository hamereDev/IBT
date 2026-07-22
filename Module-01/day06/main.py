# day06/main.py

class SMSAlert:
    def update(self, message):
        print(f'SMS ALERT: {message}')


class Account:
    def __init__(self, owner, account_number, balance=0):
        self.owner = owner
        self.account_number = account_number
        self._balance = balance
        self.observers = []

    @property
    def balance(self):
        return self._balance

    def attach(self, observer):
        self.observers.append(observer)

    def notify(self, message):
        for obs in self.observers:
            obs.update(message)

    def deposit(self, amount):
        self._balance += amount
        self.notify(f'{self.owner} deposited {amount} ETB')

    def statement(self):
        print(f'{self.owner} | Balance: {self.balance} ETB')


class SavingsAccount(Account):
    pass


class CurrentAccount(Account):
    pass


class AccountFactory:
    @staticmethod
    def create(kind, owner, number, balance=0):
        if kind == 'savings':
            return SavingsAccount(owner, number, balance)

        if kind == 'current':
            return CurrentAccount(owner, number, balance)

        raise ValueError('Unknown account type')


# Test
alert = SMSAlert()

acc1 = AccountFactory.create('savings', 'Almaz', 'S-1001', 5000)
acc2 = AccountFactory.create('current', 'Hamere', 'C-2001', 3000)

acc1.attach(alert)
acc2.attach(alert)

acc1.deposit(1000)
acc2.deposit(500)

acc1.statement()
acc2.statement()