

class Logger:
    def __init__(self) -> None:
        self.transaction_count = 0
        self.daily_sales = 0 



 #As a developer, I want to use the Singleton pattern (as shown in the Design Patterns Demo repo) 
 # to create a single instance of a Logger object inside the logger.py file and 
 # import this instance into the Franchise class to be shared by all instantiations.
   
   
   
    def log_transaction(self, order):
        self.transaction_count += 1
        self.daily_sales += order.price
