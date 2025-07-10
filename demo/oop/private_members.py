class Product:
    def __init__(self, name, price):
        self.name  = name
        # private
        self.__price = price


p1 = Product("iPhone 16", 90000)
print(p1._Product__price)
print(p1.__dict__)


