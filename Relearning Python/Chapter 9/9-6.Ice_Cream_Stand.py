"""
An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote in
Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
will work; just pick the one you like better. Add an attribute called flavors that
stores a list of ice cream flavors. Write a method that displays these flavors.
Create an instance of IceCreamStand, and call this method
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
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        """Initalize flavor with inheritance from parent class: Restaurant"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavor = flavors
        
    def read_flavor(self):
        print(f'THe flavor is {self.flavor}')
        
IceCreamRestaurant_1 = IceCreamStand('Ice Cream Shop 1', 'Ice Cream 1', 'Flavor 1')
IceCreamRestaurant_1.read_flavor()