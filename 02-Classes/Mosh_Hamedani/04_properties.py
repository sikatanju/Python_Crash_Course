# * Properties

# *** Property is an object that sits in front of an attribute, 
# *   and allows us to set and get the value of that attribute


class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        return self.__price
    
    def set_price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative.")
        
        self.__price = value

    price = property(get_price, set_price)

brush = Product(1)
# brush.price = -1
# print(brush.price)


# *** Improved implementation:

class Product:

    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price can't be negative.")
        
        self.__price = value


brush = Product(1)
brush.price = 11
print(brush.price)