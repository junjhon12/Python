def recursive_digit_sum(n):
    # Base case: if the number is a single digit, return the number itself
    if n < 10:
        return n
    else:
        # Get the last digit and add it to the sum of the rest of the digits
        return n % 10 + recursive_digit_sum(n // 10)

# Example usage
input = int(input("Enter an integer: "))  # Taking user input
result = recursive_digit_sum(input)
print(result)
