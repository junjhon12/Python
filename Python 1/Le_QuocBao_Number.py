# Define a class called Number
class Number:
    # Constructor method that initializes the instance variable num
    def __init__(self, num):
        self.num = num

    # Method that returns the string representation of the instance variable num
    def __str__(self):
        return str(self.num)

    # Method that overloads the + operator to add two Number objects
    def __add__(self, other):
        return Number(self.num + other.num)

    # Method that overloads the - operator to subtract two Number objects
    def __sub__(self, other):
        return Number(self.num - other.num)

    # Method that overloads the * operator to multiply two Number objects
    def __mul__(self, other):
        return Number(self.num * other.num)

    # Method that overloads the / operator to divide two Number objects
    def __truediv__(self, other):
        if other.num != 0:
            return Number(self.num // other.num)
        else:
            raise ValueError("Cannot divide by zero")

# Example usage
num1 = Number(int(input("Enter a number: ")))
num2 = Number(int(input("Enter another number: ")))

# Demonstrating each operator
result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
result_div = num1 / num2

# Using all 4 operators in one expression
result_combined = (result_add + result_sub * result_div) / result_mul

# Printing results
print(f"{num1} + {num2} = {result_add}")
print(f"{num1} - {num2} = {result_sub}")
print(f"{num1} * {num2} = {result_mul}")
print(f"{num1} / {num2} = {result_div}")
print(f"( {result_add} + {result_sub} * {result_div} ) / {result_mul} = {result_combined}")
