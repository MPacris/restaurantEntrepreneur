
from order_factory import OrderFactory
from logger import logger

#10 points): As a developer, I want to create a Franchise class with a place_order() method that will:
# ask a user what food they would like to order
#call the static OrderFactory.create_order() method to instantiate an order object.
#all the logger.log_transaction() method to log the order to the log.txt file

class Franchise:
    def __init__(self, location_number):
        self.location_number = int(location_number)


    def place_order(self):
        order = input(f"location- {self.location_number} choose from the following: \ntype 1 for Pizza, 2 for Pasta or 3 for Salad----   ")
        if order == '1':
            orders = OrderFactory.create_order(order) 
        elif order == '2':
            orders = OrderFactory.create_order(order)    
        elif order == '3':
            orders = OrderFactory.create_order(order) 
        else:
            print('WRONG!')
            return self.place_order()   

        
        orders = OrderFactory.create_order(order)    
        logger.log_transaction(orders, self.location_number)

      




        




    
        
        

