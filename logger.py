


class Logger:
    def __init__(self):
        self.transaction_count = 0
        self.daily_sales = 0
        

   
    def log_transaction(self, orders, location_number):
        self.daily_sales += orders.price
        self.transaction_count += 1
        file = open('log.txt','a')
        file.write(f"\n Order #{self.transaction_count}: {orders.dish_name} at location {location_number} - ${orders.price}; Total: ${self.daily_sales}\n")
        file.close()

logger = Logger()
        
       



