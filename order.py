from order_factory import OrderFactory

class Order(OrderFactory):
    def __init__(self) -> None:
        self.dish_name = ''
        self.price = int()
        pass