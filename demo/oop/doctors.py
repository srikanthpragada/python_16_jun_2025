from abc import ABC, abstractmethod


# Abstract class
class Doctor(ABC):
    def __init__(self, name, mobile, dept):
        self.name = name
        self.mobile = mobile
        self.dept = dept

    def __str__(self):
        return f"{self.name} - {self.mobile} - {self.dept}"

    @abstractmethod
    def getsalary(self):
        pass


class ResidentDoctor(Doctor):
    def __init__(self, name, mobile, dept, salary):
        super().__init__(name, mobile, dept)
        self.salary = salary

    def __str__(self):
        return super().__str__() + f" - {self.salary}"

    def getsalary(self):
        return self.salary


class Consultant(Doctor):
    def __init__(self, name, mobile, dept, visits, charge):
        super().__init__(name, mobile, dept)
        self.visits = visits
        self.charge = charge

    def __str__(self):
        return super().__str__() + f" - {self.visits} - {self.charge}"

    def getsalary(self):
        return self.visits * self.charge


rd = ResidentDoctor("Scott", "3939393333", "Card", 400000)
print(rd)

c = Consultant("Kevin", "3939393333", "ORTH", 20, 2000)
print(c.getsalary())
