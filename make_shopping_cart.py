"""
Assignment 5
Submitted by Eduard Lopushansky

Program builds a shopping cart and executes all methods defines in other modules
--------------------------------------------------------------------------------
"""
import pickle
from baby_toy import BabyToy
from frozen_dessert import FrozenDessert
from my_invoice import get_invoice
from shopping_cart import ShoppingCart

text1 = 'Testing {} method on shopping qty and inventory'
text2 = 'Shopping cart items:'
text3 = 'Testing {} method'

my_cart = ShoppingCart()
my_toy1 = BabyToy(18, 0, 100, 'Baby Toy', 'Animal Doll', 'Choking Hazard', '1 YEAR OLD +')
my_toy2 = BabyToy(40, 0, 10, 'Baby Toy', 'Kids Drum set', 'Warning:Content under pressure', '5 YEAR OLD +')
my_desert_1 = FrozenDessert(5, 0, 50, 'Frozen Dessert', 'Ice Cream', '1 quart', '-5''\u00b0''F', '10/2017')
my_desert_2 = FrozenDessert(30, 0, 20, 'Frozen Dessert', 'Baked Alaska', '3 quarts', '0''\u00b0''F', '09/2017')

my_cart.add_item(my_toy1,3)
my_cart.add_item(my_toy2,2)
my_cart.add_item(my_desert_1,5)
my_cart.add_item(my_desert_2,2)

print(__doc__)
print(text1.format('add_item'))
print('*' * len(text1.format('add_item')))
print('Expecting 3', '{}'.format(my_toy1.name), '{:>11}:'.format('Received'), my_toy1.shop_quantity,
      ' Resulted inventory qty:', my_toy1.inventory)
print('Expecting 2', '{}'.format(my_toy2.name), '{:>10}'.format('Received:'), my_toy2.shop_quantity,
      ' Resulted inventory qty:', my_toy2.inventory)
print('Expecting 5', '{}'.format(my_desert_1.name), '{:>14}'.format('Received:'), my_desert_1.shop_quantity,
      ' Resulted inventory qty:', my_desert_1.inventory)
print('Expecting 2', '{}'.format(my_desert_2.name), '{:>11}'.format('Received:'), my_desert_2.shop_quantity,
      ' Resulted inventory qty:', my_desert_2.inventory)
print()

print(text2)
print('*' * len(text2))
print(my_cart)
print(text1.format('subtract_item'))
print('*' * len(text1.format('subtract_item')))

my_cart.subtract_item(my_toy1)
my_cart.subtract_item(my_desert_1,2)

print('Expecting 2', '{}'.format(my_toy1.name), '{:>11}:'.format('Received'), my_toy1.shop_quantity,
      ' Resulted inventory qty:', my_toy1.inventory)
print('Expecting 3', '{}'.format(my_desert_1.name), '{:>14}'.format('Received:'), my_desert_1.shop_quantity,
      ' Resulted inventory qty:', my_desert_1.inventory)
print()

print(text3.format('get_subtotal'))
print('*' * len(text3.format('get_subtotal')))
print('Expecting cart subtotal of 151', '{:>11}:'.format('Received'), my_cart.subtotal)
print()

print(text3.format('set_age_group'))
print('*' * len(text3.format('set_age_group')))
my_toy1.set_age_group('2 YEARS OLD +')
print('Expecting age group of Animal Doll to be changed from 1 YEARS OLD + to 2 YEARS OLD+', ' Received: ',
      my_toy1.age_group)
print()

print(text3.format('set_exp_date'))
print('*' * len(text3.format('set_exp_date')))
my_desert_1.set_exp_date('11/2017')
print('Expecting expiration date of Ice Cream to be changed from 10/2017 to 11/2017', ' Received: ',
      my_desert_1.exp_date)
print()
print('-' * 100)
print()


# creating pickle file  for my_cart object
def write_to_pickle(my_cart):
    with open('my_cart.pkl', 'wb') as datafile:
        pickle.dump(my_cart, datafile)

    with open('my_cart.pkl', 'rb') as datafile:
        my_pickled_cart = pickle.load(datafile)
        return my_pickled_cart


print('Reading my_cart from pickle file')
print('*' * len('Reading my_cart from pickle file'))
my_pickle_file = write_to_pickle(my_cart)
print(my_pickle_file)

get_invoice(my_cart)


if __name__ == '__main__':
    pass
