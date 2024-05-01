"""
Make a class Die with one attribute called sides, which has a
default value of 6. Write a method called roll_die() that prints a random number between 1 and the number of sides the die has. Make a 6-sided die and
roll it 10 times.
Make a 10-sided die and a 20-sided die. Roll each die 10 times.
"""
from random import randint
class Die:
    def __init__(self, sides):
        self.sides = 6
        
    def roll_die(self):
        print(randint(1, self.sides))
        
    def ten_times(self):
        numList = list()
        i = 0
        while i != 10:
           numList.append(randint(1, self.sides)) 
           i += 1
        print(numList)
        
    def ten_sided(self):
        numList = list()
        self.sides = 10
        i = 0
        while i != 10:
            numList.append(randint(1, self.sides))
            i += 1
        print(numList)
            
    def twenty_sided(self):
        numList = list()
        self.sides = 20
        i = 0
        while i != 10:
            numList.append(randint(1, self.sides))
            i += 1
        print(numList)
            
        
die1 = Die('')
die1.roll_die()
print()
die1.ten_times()
die1.twenty_sided()