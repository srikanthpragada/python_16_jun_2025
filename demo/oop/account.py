class SavingsAccount:
    def __init__(self, acno, customer, balance):
        self.acno = acno
        self.customer = customer
        self.balance = balance

    def deposit(self, amount):
        self.balance  += amount

    def withdraw(self, amount):
        self.balance -= amount

    def getbalance(self):
        return self.balance


a1 = SavingsAccount(1, "George", 25000)
a1.deposit(10000)
a1.withdraw(5000)
print(a1.getbalance())

a2 = SavingsAccount(2, 'Mark', 10000)
print(a2.getbalance())


