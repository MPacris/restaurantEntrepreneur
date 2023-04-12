
from logger import Logger
from order_factory import OrderFactory



class Franchise:
    def __init__(self) -> None:
        self.location_number = int()
        pass

    def place_order(self):
        self.order = OrderFactory.create_order()
        
        

