

#As a developer, I want to create an Order parent class 
# and 3 child classes to represent menu items of my choosing

class Order:
    def __init__(self, name, price) -> None:
        self.dish_name = name
        self.price = int(price)      
    
    

