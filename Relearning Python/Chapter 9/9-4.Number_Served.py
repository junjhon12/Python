"""
 Start with your program from Exercise 9-1 (page 162).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of
customers that have been served. Call this method with a new number and print
the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a day of
business.
"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name and cuisine type"""
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        """Describe the restaurant and it's cuisine type"""
        print(f"{self.name} seems to be")
        print(f"Outdated and Old fashion that serves {self.type}")
        
    def open_restaurant(self):
        """Let user know if restaurant is open or not"""
        print(f'{self.name} is open')
    
    def set_number_served(self, serving):
        """Number served is set a new value"""
        print(f'New value set: {serving}')
        self.number_served = serving
    
    def increment_number_served(self, serving):
        """Number served is added"""
        print(f'{serving} was added')
        self.number_served += serving    
        
    def read_served(self):
        """Print number of servings"""
        print(f'{self.name} served {self.number_served}')
        
restaurant1 = Restaurant('Restaurant 1', 'Cuisine1')
restaurant1.set_number_served(1)
restaurant1.read_served()
restaurant1.increment_number_served(2)
restaurant1.read_served()