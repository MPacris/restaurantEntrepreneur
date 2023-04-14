from pasta import Pasta
from pizza import Pizza
from salad import Salad


class OrderFactory:
#As a developer, I want to utilize a Factory Pattern in the create_order() method to instantiate instances of the three different Order child classes.
#This method should accept a string as a parameter (ex “Pizza”) and return the corresponding type of Order child class instantiation (ex Pizza() )
    @staticmethod
# As a developer, I want to create an Order Factory class with a static create_order method.

    def create_order(order):

        if order == '1':
            return Pizza()
        elif order == '2':
            return Pasta()
        elif order == '3':
            return Salad()


       



      
