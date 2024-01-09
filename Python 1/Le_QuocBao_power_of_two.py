def is_power_of_two(n):
    # Base case: if n is 1, it's a power of two
    if n == 1:
        return True
    # If n is not divisible by 2 or it's 0, it's not a power of two
    elif n % 2 != 0 or n == 0:
        return False
    else:
        # Recursively check if n divided by 2 is a power of two
        return is_power_of_two(n // 2)

# Example usage
num = int(input("Enter an integer: "))  # Taking user input
result = is_power_of_two(num)  # Checking if the input number is a power of two
print(f"Output: {result}")  # Displaying the result
