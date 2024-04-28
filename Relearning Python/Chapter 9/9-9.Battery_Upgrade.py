"""
Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 65 if it isn’t already. Make
an electric car with a default battery size, call get_range() once, and then
call get_range() a second time after upgrading the battery. You should see an
increase in the car’s range.
"""
class Car:
    """Represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_description(self):
        """Return descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles
        
class Battery:
    """Model a battery for an electric car"""
    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can go about {range} miles on a full charge.")   
        
    def upgrade_battery(self):
        if self.battery_size != 65:
           self.battery_size = 65
        print(f"Battery size is now {self.battery_size}")          
        
class ElectricCar(Car):
    """Represent aspects of a electric vehicle"""
    def __init__(self, make, model, year):
        """Initialize attributes of parent class."""
        super().__init__(make, model, year)
        self.battery_size = 40
        self.battery = Battery()
        
    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
        
    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")
        
car1 = ElectricCar('Make1', 'Model1', 2000)
car1 = Battery()
car1.get_range()
car1.upgrade_battery()
car1.get_range()