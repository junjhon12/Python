"""
Make a list or tuple containing a series of 10 numbers and 5 letters.
Randomly select 4 numbers or letters from the list and print a message saying that
any ticket matching these 4 numbers or letters wins a prize.
"""
from random import choice

A = ("One", "Two", "Three", "Four", "Five", 1, 2, 3, 4, 5)

win = list()
i = 0
while i != 4:
    win.append(choice(A))
    i += 1
print('Any ticket matching these 4 numbers or letters wins a prize:' + str(win))