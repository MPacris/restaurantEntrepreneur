
from order_factory import OrderFactory
from logger import Logger



class Franchise:
    def __init__(self,location_number) -> None:
        self.location_number = location_number
        pass

    def place_order(self):
        user_choice = (f"choose from the following: Pizza, Pasta or Salad----   ")
        order = OrderFactory.create_order(user_choice)
        Logger.log_transaction(order, self.location_number)





        




    
        
        

