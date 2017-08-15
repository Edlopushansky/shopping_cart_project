"""
Module defines a FrozenDessert class ( subclass of Food and Product classes ) with variables: name, size, refreg_temp
exp_date and one class method set_exp_date
"""

from food import Food
from product import Product


class FrozenDessert(Food, Product):
    def __init__(self, price, shop_quantity, inventory, prod_category, name, size, refrig_temp, exp_date):
        Product.__init__(self, price, shop_quantity, inventory, prod_category)
        Food.__init__(self)
        self.name = name
        self.size = size
        self.refrig_temp = refrig_temp
        self.exp_date = exp_date

    def set_exp_date(self, exp_date):
        self.exp_date = exp_date

    def __str__(self):
        return '{name}'.format(name = self.name)+ Product.__str__(self)+ \
               'Size: {size}\nRefrigeration temperature: {temp}\nExpiration date: {exp}'.\
                   format(size=self.size, temp=self.refrig_temp,exp=self.exp_date)

if __name__ == '__main__':
    prod = FrozenDessert(5, 1, 49, 'Frozen Dessert', 'Ice Cream', '1 quart', '-5''\u00b0''F', '09/2017')
    print(prod)
    print()
    prod.set_exp_date('10/2018')
    print(prod)
