class Food:
    
    all = []

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Food.all.append(self)

    @classmethod
    def food_names(cls):
        return [food.name for food in cls.all]
    
    @classmethod
    def average_price(cls):
        if len(cls.all) == 0:
            return 0
        else:
            price_list = [food.price for food in cls.all]
            return sum(price_list) / len(price_list)
    
    @classmethod
    def most_expensive(cls):
        if len(cls.all) == 0:
            return None
        else:
            return max(cls.all, key=lambda f:f.price)