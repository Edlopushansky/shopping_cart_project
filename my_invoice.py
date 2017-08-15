"""
This module defines a get_invoice function that takes a my_cart object and prints it out an invoice
"""
from baby_toy import BabyToy
from frozen_dessert import FrozenDessert
from shopping_cart import ShoppingCart


def get_invoice(cart):
    print('\033[4mInvoice:\033[0m\nYour Order was placed\nThank you for your order!\n')
    print('{:>9}{:>15}{:>15}{:^15}'.format('Item', 'Quantity', 'Unit price', 'Amount'))
    for item in cart.item_list:
        print(item.name.rjust(13),repr(item.shop_quantity).center(12),repr(item.price).rjust(7),
              repr(item.price * item.shop_quantity).rjust(12))
    print('{:>44}'.format('Total $:'), cart.subtotal)



if __name__ == '__main__':
    my_cart = ShoppingCart()
    my_toy1 = BabyToy(18, 1, 100, 'Baby Toy', 'Animal Doll', 'Choking Hazard', '1 YEAR OLD +')
    my_toy2 = BabyToy(40, 1, 10, 'Baby Toy', 'Kids Drum set', 'Warning:Content under pressure', '5 YEAR OLD +')
    my_desert_1 = FrozenDessert(5, 1, 50, 'Frozen Dessert', 'Ice Cream', '1 quart', '-5''\u00b0''F', '10/2017')
    my_desert_2 = FrozenDessert(30, 1, 20, 'Frozen Dessert', 'Baked Alaska', '3 quarts', '0''\u00b0''F', '09/2017')

    my_cart.add_item(my_toy1,3)
    my_cart.add_item(my_toy2,2)
    my_cart.add_item(my_desert_1,2)
    my_cart.add_item(my_desert_2)

    print('{:>9}{:>15}{:>15}{:^15}'.format('Item', 'Quantity', 'Unit price', 'Amount'))
    for item in my_cart.item_list:
        print(item.name.rjust(13),repr(item.shop_quantity).center(12),repr(item.price).rjust(7),
              repr(item.price * item.shop_quantity).rjust(12))
    print('{:>44}'.format('Total $:'),my_cart.subtotal)