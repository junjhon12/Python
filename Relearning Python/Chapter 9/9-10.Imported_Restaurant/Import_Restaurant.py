"""
Using your latest Restaurant class, store it in a module. Make a separate file that imports Restaurant. Make a Restaurant instance,
and call one of Restaurant’s methods to show that the import statement is working properly.
"""

from Restaurant import *

restaurant2 = Restaurant('Restaurant2', 'Cuisine2')
print(restaurant2.describe_restaurant())