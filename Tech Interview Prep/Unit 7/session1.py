"""
Problem 1: Hello Hello
"""
def repeat_hello(n):
    if n > 0:
        print("Hello")
        repeat_hello(n-1)
repeat_hello(5)
print()
def repeat_hello_iterative(n):
    count = 1  # Initialize the counter to 1
    while count <= n:  # Loop until count exceeds n
        print("Hello")
        count += 1  # Increment the counter by 1
repeat_hello_iterative(5)
print()
"""
Problem 2: Factorial Cases
"""
def factorial(n):
    i = 1
    output = 1 # Initialize the output to 1 (since factorial of 0 is 1)
    while i <= n: # Loop until i exceeds n
        output *= i # Multiply output by i to compute factorial
        i += 1  # Increment the counter by 1
    return output
print(factorial(5))
print()
"""
Problem 3: Recursive Sum
"""
def sum_list(lst) :
    # if the list is empty, return 0
    if not lst:
        return 0
    # Recursive case: sum the first element with the sum of the rest of the list
    return lst[0] + sum_list(lst[1:])
lst = [1, 2, 3, 4, 5]
print(sum_list(lst))
print()
"""
Problem 4: Recursive Power of 2
"""
def is_power_of_two(n):
    if n <= 0:
        return False
    if n == 1:
        return True
    if n % 2 != 0 :
        return False
    return is_power_of_two(n // 2)
print(is_power_of_two(2))  
print(is_power_of_two(3))  
print()
"""
Problem 5: Binary Search I
"""
def binary_search(lst, target):
    left_point = 0 # Initialize the left pointer to the start of the list
    right_point = len(lst) - 1  # Initialize the right pointer to the end of the list
    
    while left_point <= right_point :
        middle_point = (right_point + left_point) // 2  # Calculate the middle point
        
        if lst[middle_point] == target:
            return middle_point
        elif lst[middle_point] < target:  # If the target is greater, ignore the left half
            left_point = middle_point + 1
        else:  # If the target is smaller, ignore the right half
            right_point = middle_point - 1
    return -1

lst = [1, 3, 5, 7, 9, 11, 13, 15]
print(binary_search(lst, 11))
print()
"""
Problem 6: Backwards Binary Search
"""
def find_last(lst, target):
    