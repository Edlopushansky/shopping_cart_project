"""
Module defines a ShoppingCart class with three class methods "add_item" , " subtract_item" and "get_subtotal"
"""
from frozen_dessert import FrozenDessert
from baby_toy import BabyToy


class ShoppingCart:
    def __init__(self):
        self.item_list = []
        self.subtotal = 0

    def add_item(self, product, num = 1):
        if product in self.item_list:
            product.shop_quantity += num
            product.inventory -= num
            self.subtotal += product.price*num

        else:
            self.item_list.append(product)
            product.inventory -= num
            product.shop_quantity = num
            self.subtotal += product.price*num

    def subtract_item(self, product, num=1):
        if product in self.item_list:
            product.inventory += num
            product.shop_quantity -= num
            self.subtotal = self.subtotal - product.price

        else:
            self.item_list.remove(product)

    def get_subtotal(self):
        return self.subtotal

    def __str__(self):
        returned_string = ""
        for item in self.item_list:
            returned_string = returned_string + '\n' + str(item) + '\n'
        return returned_string

if __name__ == '__main__':

    my_cart = ShoppingCart()
    my_toy1 = BabyToy(18, 0, 100, 'Baby Toy','Animal Doll', 'Choking Hazard', '1 YEAR OLD +')
    my_toy2 = BabyToy(40, 0, 5, 'Baby Toy','Kids Drum Set', 'Warning:Content under pressure', '5 YEAR OLD +')
    desert_1 = FrozenDessert(5, 0, 50, 'Frozen Dessert','Ice Cream', '1 quart', '-5''\u00b0''F', '10/2017')
    desert_2 = FrozenDessert(30, 0, 10, 'Frozen Dessert','Baked Alaska', '3 quarts','0''\u00b0''F', '09/2017')

    my_cart.add_item(my_toy1)
    my_cart.add_item(my_toy2, 3)
    my_cart.add_item(desert_1)
    my_cart.add_item(desert_2, 3)

    print('Expecting 1', '{}'.format(my_toy1.name), '{:>13}:'.format('Received'), my_toy1.shop_quantity)
    print('Expecting 3', '{}'.format(my_toy2.name), '{:>12}'.format('Received:'), my_toy2.shop_quantity)
    print('Expecting 1', '{}'.format(desert_1.name), '{:>16}'.format('Received:'),desert_1.shop_quantity)
    print('Expecting 3', '{}'.format(desert_2.name), '{:>13}'.format('Received:'), desert_2.shop_quantity)
    my_cart.subtract_item(my_cart.item_list[1])
    print(my_cart)
    print('Expecting 2', '{}'.format(my_toy2.name), '   Received:', my_toy2.shop_quantity)


