class Food:
    
    # Deliverable # 2 solution code
    all = []

    # Deliverable # 1 solution code
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
        # Deliverable # 2 solution code
        Food.all.append(self)

    # Deliverable # 3 solution code
    @classmethod
    def food_names(cls):
        return [element.name for element in cls.all]
    
    # Deliverable # 4 solution code
    @classmethod
    def average_price(cls):
        price_list = [element.price for element in cls.all]
        return sum(price_list) / len(price_list)
    
    # Bonus Deliverable solution code
    @classmethod
    def most_expensive(cls):
        # Here's an algorithm that we can use to solve this Deliverable
        # most_expensive_food = None
        # for element in cls.all:
        #     if most_expensive_food == None:
        #         most_expensive_food = element
        #     else:
        #         if element.price > most_expensive_food.price:
        #             most_expensive_food = element
        
        # return most_expensive_food
    
        # We can also use the built-in max() function to solve this Deliverable
        if len(cls.all) == 0:
            return None
        else:
            return max(cls.all, key=compare_function)
        
# Bonus Deliverable solution code (compare_function() function code)
def compare_function(f):
    return f.price