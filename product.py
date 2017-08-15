"""
Module defines a Product class with class variables : price, shop_quantity, inventory, prod_category and one class
method "set_price"
"""


class Product:
    def __init__(self, price, shop_quantity, inventory, prod_category):
        self.price = price
        self.shop_quantity = shop_quantity
        self.inventory = inventory
        self.prod_category = prod_category

    def set_price(self, price):
        self.price = price

    def __str__(self):
        return '\nPrice: {price}\nShopping Quantity: {shop}\nInventory: {inv}\nCategory: {categ}\n'.\
            format(price=self.price,shop=self.shop_quantity, inv=self.inventory,categ=self.prod_category)


if __name__ == '__main__':
    prod_1 = Product(18, 2, 95, 'Baby Toy')
    print(prod_1)

    prod_1.set_price(34)

    print(prod_1.price)