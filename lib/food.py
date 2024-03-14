import ipdb

class Food:

    # Deliverable 2
    all = []
    
    # Deliverable 1
    def __init__(self, name, price):
        self.name = name
        self.price = price

        # Deliverable 2
        Food.all.append(self)

    # Deliverable 3
    @classmethod
    def food_names(cls):
        food_names_list = [food.name for food in cls.all]
        return food_names_list
    
    # Deliverable 4
    @classmethod
    def average_price(cls):
        prices_list = [food.price for food in cls.all]
        average_price = sum(prices_list) / len(prices_list)
        return round(average_price, 2)
    
    # Deliverable 5
    @classmethod
    def most_expensive(cls):
        return max(cls.all, key = lambda f: f.price)