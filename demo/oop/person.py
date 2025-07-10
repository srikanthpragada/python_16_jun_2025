class Person:
    #Special Methods
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return f"{self.name} - {self.email}"

    def __eq__(self, other):
        return self.name == other.name and self.email == other.email

    def __gt__(self, other):
        return self.name > other.name


p1 = Person("Rossum", "rossum@python.org")
p2 = Person("Rossum", "rossum@python.org")
p3 = Person("Gosling", "gosling@aws.com")

# print(p1)
# print(str(p1))
# print(p1.__str__())

# print(p1 == p2)  # p1.__eq__(p2)
# print(p1 > p3)
# print(p1 < p3)

people = [ p1, Person("Larry", "larry@gmail.com"), p3]

for p in sorted(people):
    print(p)




