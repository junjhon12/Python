"""
Problem 1: Long Pressed
Write a function is_long_pressed() that takes in a string name and a string typed as parameters. Imagine your friend is typing their name into a keyboard and when typing a character, the key might get long pressed and the character will be typed 1 or more times.

The function should examine the typed characters and return True if it is possible that it was your friends name with some characters being long pressed and False otherwise.

Use the two-pointer approach to solve the problem, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. A common variation of this technique is to point one variable at the beginning of one string and a second pointer at the beginning of a second string, then increment each pointer conditionally to solve a problem.
"""
def is_long_pressed(name, typed):
    # Initialize two pointers for name and typed strings
    name_start, typed_start = 0, 0
    # Traverse through the 'typed' string
    while typed_start < len(typed) :
        # If the current characters in both strings match, move both pointers
        if name_start < len(name) and name[name_start] == typed[typed_start] :
            name_start += 1
         # If characters do not match and it's not a long press scenario, return False
        elif typed_start == 0 or typed[typed_start] != typed[typed_start - 1] :
            return False
        # If the current character in 'typed' matches the previous character in 'typed',
        # it's a long press, so move the 'typed' pointer only
        typed_start += 1
    # After traversing 'typed', check if all characters in 'name' were matched
    return name_start == len(name)
name = "alex"
typed = "aaleex"
print(is_long_pressed(name, typed))
name2 = "saeed"
typed2 = "ssaaedd"
print(is_long_pressed(name2, typed2))
name3 = "courtney"
typed3 = "courtney"
print(is_long_pressed(name3, typed3))
print()

"""
Problem 2: Sharing Cookies
Imagine you're an awesome babysitter and want to give the kids you're looking after some cookies as a snack.
Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with.
Each cookie j has a cookie size s[j].
If s[j] >= g[i], we can assign the cookie j to the child i, and the child will be content.
If s[j] < g[i], the child will not be content.

Write a function find_content_children() that takes in the greed list g and the cookie size list s as parameters and maximizes the number of content children you are babysitting! The function returns
"""

def find_content_children(g, s) :
    # Initialize pointers for greed factors and cookie sizes
    child_i = 0
    cookie_j = 0
    
    # Iterate through both lists
    while child_i < len(g) and cookie_j < len(s):
        # If the current cookie can satisfy the current child
        if s[cookie_j] >= g[child_i]:
            # Move to the next child
            child_i += 1
        # Move to the next cookie
        cookie_j += 1
    
    # The number of content children is equal to the pointer of greed factors
    return child_i

g = [1,2,3] #Greed
s = [1,1,3] #Cookie
print(find_content_children(g,s)) # Output: 2 
g = [1,1]
s = [2,2,2]
print(find_content_children(g,s)) # Output: 2 
print()

"""
Problem 3: Valid Palindrome
Write a function valid_palindrome() that takes in a string s as a parameter and returns True if s can be a palindrome after deleting at most one character from it and False otherwise.
"""
'''
def palidrome_check(s) :
    start = 0
    end = len(s) - 1
    count = 0
    while start < end :
        if s[start] == s[end] :
            count += 1
            end += 1
        start += 1
    return count
        
def valid_palindrome(s):
    if palidrome_check(s) >= 1 :
        return True
    return False
s = "aba"
s2 = "abca"
s3 = "abc"
print(valid_palindrome(s))
print(valid_palindrome(s2))
print(valid_palindrome(s3))
'''

Given a list of int nums and int k, write a function to find the minimum sum of any contaguous sublist of size k. If the size of the nums is less than k, return 0.
nums = [5, -1, 3, 2 ,-4], k =2
output: -3
def find_min_sublist_sum(nums, k):