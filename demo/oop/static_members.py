class Product:
    # static or class attribute
    taxrate = 12
    def __init__(self, name, price):
        # object attributes
        self.name  = name
        self.price = price

    def netprice(self):
        return self.price + self.price * Product.taxrate / 100

    @staticmethod
    def gettaxrate():
        return Product.taxrate


p1 = Product("iPhone 16", 90000)
print(p1.netprice())

print(Product.gettaxrate())





