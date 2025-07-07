class Counter:
    #constructor
    def __init__(self, value = 0):
        # Object Attribute
        self.value = value

    # Methods
    def increment(self):
        self.value += 1

    def decrement(self):
        self.value -= 1

    def getvalue(self):
        return self.value

# Objects or Instances
c1 = Counter(100)   # __init__(100) is called
c1.increment()
# print(c1.value)
print(c1.getvalue())

c2 = Counter()
print(c2.getvalue())

print(type(c2))

print(type("Abc"))