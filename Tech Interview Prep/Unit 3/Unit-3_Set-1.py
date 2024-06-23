"""
Problem 1: Calling Mississippi
"""
def count_mississippi(limit):
    for num in range(1, limit):
	    print( f"{num} mississippi")

limit = 6
print(count_mississippi(limit))
print()

"""
Problem 2: Swap Ends
Write a function swap_ends() that accepts a string my_str as a parameter and returns a new string where the first and last characters from my_str are swapped.
"""
def swap_ends(my_str) :
    # Alway's get the first char
    first_letter = my_str[0]
    # Alway's get the last char
    last_letter = my_str[-1]
    # Alway's get the character's between first and last
    in_between = my_str[1:-1]
    return last_letter + in_between + first_letter
my_str = "boat"
swapped = swap_ends(my_str)
print(swapped)
print()

"""
Problem 3: Is Pangram
Write a function is_pangram() that takes in a string my_str as a parameter and returns True if the string is a pangram and False if not. A pangram is a sentence containing every letter in the English alphabet.
"""
def is_pangram(my_str):
    num_Alphabet = 26
    char_collector = {}
    for i in my_str.low() :
        
    
    
my_str = "The quick brown fox jumps over the lazy dog"
print(is_pangram(my_str))
str2 = "The dog jumped"
print(is_pangram(str2))