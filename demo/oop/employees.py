class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def getsalary(self):
        return self.salary

    def show(self):
        print(self.name)
        print(self.salary)


class OnsiteEmployee(Employee):
    def __init__(self, name, salary, allowance):
        super().__init__(name, salary)
        self.allowance = allowance

    def show(self):
        super().show()
        print(self.allowance)

    def getsalary(self):
        return self.salary + self.allowance


oe = OnsiteEmployee("Ellison", 200000, 100000)
print(oe.getsalary())
oe.show()
