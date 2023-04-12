class Logger:
    def __init__(self) -> None:
        self.transaction_count = int()
        self.daily_sales = int()
        pass
 #As a developer, I want to use the Singleton pattern (as shown in the Design Patterns Demo repo) 
 # to create a single instance of a Logger object inside the logger.py file and 
 # import this instance into the Franchise class to be shared by all instantiations.
   
   
   
    def log_transaction(self,order):
        self.order = order

        pass

    def write_to_file(message):
        file = open('log.txt', "a")
        file.write(message)
        file.close()
        pass
