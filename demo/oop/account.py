class InvalidAmountError(Exception):
    def __init__(self, amount):
        super().__init__(f'Invalid Amount : {amount}')


class SavingsAccount:
    def __init__(self, acno, customer, balance = 0):
        self.acno = acno
        self.customer = customer
        if balance < 0:
            raise ValueError('Invalid Initial Balance. It must be >= 0')

        self.balance = balance

    def deposit(self, amount):
        if amount > 0 :
            self.balance  += amount
        else:
            raise InvalidAmountError(amount)


    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            raise ValueError('Insufficient Balance')

    def getbalance(self):
        return self.balance

try:
    a1 = SavingsAccount(1, "George", 25000)
    a1.deposit(-10000)
    a1.withdraw(50000)
    print(a1.getbalance())
except Exception as ex:
    print(ex)

a2 = SavingsAccount(2, 'Mark', 10000)
print(a2.getbalance())


