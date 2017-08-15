"""
Module defines an abstract class Food with one class method
"""
import abc


class Food(metaclass=abc.ABCMeta):
    """
    Definition of an abstract method
    """
    @abc.abstractmethod
    def set_exp_date(self,date):
        return
