"""
You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write
a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.
"""
from random import randint
my_ticket = (1)
win = False
tries = 1
while win == False:
    number = randint(1, 3)
    print(number)
    if number == my_ticket:
        win = True
        print('It took: ' + str(tries) + ' tries to get ' + str(my_ticket))
    tries += 1
    