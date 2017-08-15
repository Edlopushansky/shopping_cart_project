"""
Defines an abstract class Toy with one class method
"""

import abc


class Toy(metaclass=abc.ABCMeta):
    """
    Definition of an abstract method
    """
    @abc.abstractmethod
    def set_age_group(self,age):
        return

