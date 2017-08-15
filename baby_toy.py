"""
Module defines a BabyToy class ( subclass of Toy and Product classes ) with variables: name, safety_info, age_group
and one class method set_age_group
"""
from toy import Toy
from product import Product


class BabyToy(Toy, Product):

    def __init__(self, price, quantity, inventory, category, name, safety_info, age_group):
        Toy.__init__(self)
        Product.__init__(self, price, quantity, inventory, category)
        self.name = name
        self.safety_info = safety_info
        self.age_group = age_group

    def set_age_group(self,age_group):
        self.age_group = age_group

    def __str__(self):
        return '{name}'.format(name=self.name)+ Product.__str__(self)+'Safety Info: {info}\nAge Group: {age}'.\
            format(info=self.safety_info, age=self.age_group)


if __name__ == '__main__':
    my_toy = BabyToy(18, 2, 95, 'Baby Toy','Animal Doll', 'Chocking hazard', '1 y.o +')
    print(my_toy)
    my_toy.set_age_group('10+')
    print(my_toy)
