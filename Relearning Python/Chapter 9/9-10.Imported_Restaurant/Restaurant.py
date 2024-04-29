"""
Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.name = restaurant_name
        self.type = cuisine_type
        
    def describe_restaurant(self):
        """Describe the restaurant and it's cuisine type"""
        print(f"{self.name} seems to be outdated and Old fashion that serves {self.type}")
        
    def open_restaurant(self):
        """Let user know if restaurant is open or not"""
        print(f'{self.name} is open')
        
