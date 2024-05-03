"""
One common problem when prompting for numerical input
occurs when people provide text instead of numbers. When you try to convert
the input to an int, you’ll get a ValueError. Write a program that prompts for
two numbers. Add them together and print the result. Catch the ValueError if
either input value is not a number, and print a friendly error message. Test your
program by entering two numbers and then by entering some text instead of a
number.
"""

class add_number:
    def __init__(self):
        pass
    
    def add(self):
        while True:
            num1 = input('Enter number 1: ')
            if num1 == 'quit':
                break
            num2 = input('Enter number 2: ')
            if num2 == 'quit':
                break
            try:
                result = int(num1) + int(num2)
            except ValueError:
                print('Please enter a valid number')
            else:
                print(result)

test0 = add_number()
test0.add()