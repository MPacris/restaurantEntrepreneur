
from order_factory import OrderFactory
from logger import logger



class Franchise:
    def __init__(self, location_number):
        self.location_number = int(location_number)


    def place_order(self):
        order = input(f"{self.location_number} -- choose from the following: Pizza, Pasta or Salad----   ")
        orders = OrderFactory.create_order(order)
        logger.log_transaction(orders, self.location_number)

      




        




    
        
        

