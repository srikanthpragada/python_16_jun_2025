class Counter:
    #constructor
    def __init__(self, value = 0):
        # Object Attribute
        self.value = value
        self.initvalue = value

    # Methods
    def increment(self):
        self.value += 1

    def decrement(self):
        if self.value > 0:
           self.value -= 1
        else:
            print("Cannot decrement below 0")

    def getvalue(self):
        return self.value

    def reset(self):
        self.value = self.initvalue

# Objects or Instances
c1 = Counter(100)   # __init__(100) is called
c1.increment()
c1.reset()

# print(c1.value)
print(c1.getvalue())

c2 = Counter()
print(c2.getvalue())

print(type(c2))

print(type("Abc"))