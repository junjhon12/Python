"""
Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.name = restaurant_name
        self.type = cuisine_type
        
    def describe_restaurant(self):
        """Describe the restaurant and it's cuisine type"""
        print(f"{self.name} is popular and serves {self.type}")
        
    def open_restaurant(self):
        """Let user know if restaurant is open or not"""
        print(f'{self.name} is open')
        
        
restaurant1 = Restaurant('Restaurant1', 'Cuisine1')
restaurant1.describe_restaurant()

restaurant2 = Restaurant('Restaurant2', 'Cuisine2')
restaurant2.describe_restaurant()

restaurant3 = Restaurant('Restaurant3', 'Cuisine3')
restaurant3.describe_restaurant()