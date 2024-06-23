"""
Problem 1: Prime Number
Write a function is_prime() that takes in a positive integer n and returns True if it is a prime number and False otherwise. A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
"""
def is_prime(n) :
    if n > 1:
        # Iterate from 2 to n // 2
        for i in range(2, (n//2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (n % i) == 0:
                return False
                break
        else:
            return True
    else:
        return False
print(is_prime(5))
print(is_prime(-12))
print(is_prime(9))
print()

"""
Problem 2: Two-Pointer Reverse List
Write a function reverse_list() that takes in a list lst and returns elements of the list in reverse order. The list should be reversed in-place without using list slicing (e.g. lst[::-1]).

Instead, use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.
"""
def reverse_list(lst) :
    start = 0
    end = len(lst) - 1
    while start < end :
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
            
lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))

"""
Problem 3: Evaluating Solutions
The reverse_list() problem can also be solved without using the two pointer technique (as you may have seen it in previous units)! Evaluate the time and space complexity of your two-pointer solution.

Then, evaluate the time and space of the following solution:

def reverse_list(lst):
    # Create a new reversed list
    reversed_lst = lst[::-1]
    # Copy the elements back into the original list
    for i in range(len(lst)):
        lst[i] = reversed_lst[i]
Which has better time complexity?
Which has better space complexity?
"""

"""
Problem 4: Move Even Integers
Write a function sort_list_by_parity() that takes in an integer list nums as a parameter and moves all the even integers at the beginning of the list followed by all the odd integers. The function returns any list that satisfies this condition.
"""
def sort_array_by_parity(nums):
    start = 0
    end = len(nums) - 1
    while start < end :
        if nums[start] % 2 != 0 and nums[end] % 2 == 0 :
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        elif nums[start] % 2 == 0 :
            start += 1
        elif nums[end] % 2 != 0 :
            end -= 1
    return nums
    
nums = [3,1,2,4]
nums2 = [0]
print(sort_array_by_parity(nums))
print(sort_array_by_parity(nums2))
print()

"""
Problem 5: Palindrome
Write a function first_palindrome() that takes in a list of strings words as a parameter and returns the first palindromic string in the list. A string is palindromic if it reads the same forward and backward. If there is no such string, return an empty string ""
"""
def first_palindrome(words):
    for word in words:
        start, end = 0, len(word) - 1  # Initialize pointers to the start and end of the word
        is_palindrome = True  # Assume the word is a palindrome
        while start < end:
            if word[start] != word[end]:  # If characters at start and end don't match
                is_palindrome = False  # Mark as not a palindrome
                break  # Exit the while loop early
            start += 1  # Move start pointer to the right
            end -= 1  # Move end pointer to the left
        if is_palindrome:
            return word  # Return the word if it is a palindrome
    return ' '  # Return a space if no palindrome is found
    
words = ["abc","car","ada","racecar","cool"]
palindrome1 = first_palindrome(words)
print(palindrome1)

words2 = ["abc","racecar","cool"]
palindrome2 = first_palindrome(words2)
print(palindrome2)

words3 = ["abc", "def", "ghi"]
palindrome3 = first_palindrome(words3)
print(palindrome3)
print()

"""
Problem 6: Remove Duplicates with O(1)
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes the duplicates in-place such that each element appears only once. Do not allocate extra space for another array; you must do this by modifying the input list with O(1) extra memory. The function returns the new length of the list.
"""
# check if start == end
    # Yes = remove.start then end -= 1
    # No = end -= 1

def remove_duplicates(nums):
    if not nums:
        return 0
    
    write_index = 1
    
    for i in range(1, len(nums)):
        if nums[i] != nums[write_index - 1]:
            nums[write_index] = nums[i]
            write_index += 1
    
    return write_index

# Example usage:
nums = [1, 1, 2, 3, 4, 4, 4, 5]
print(nums)
new_length = remove_duplicates(nums)
print(new_length)
print(nums[:new_length])  # slicing to show the result with unique elements
print()

"""
Problem 1: Perfect Number
Write a function is_perfect_number() that takes in a positive integer n and returns True if it is a perfect number and False otherwise. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding itself.

For example, 6 is a perfect number because its divisors or 1, 2, and 3 and 1 + 2 + 3 = 6.
"""
def is_perfect_number(n):
    if not n:
        None
    i = 0
    j = 1
    while i <= n :
        i = i + (j)
        j += 1
        if i == n :
            return True
    return False   
print(is_perfect_number(6))
print(is_perfect_number(28))
print(is_perfect_number(9))
print()

"""
Problem 2: 2-Pointer Palindrome
Write a function is_palindrome() that takes in a string s as a parameter and returns True if the string is a palindrome and False otherwise. You may assume the string contains only lowercase alphabetic characters.

The function must use the two-pointer approach, which is a common technique in which we initialize two variables (also called a pointer in this context) to track different indices or places in a list or string, then moves the pointers to point at new indices based on certain conditions. In the most common variation of the two-pointer approach, we initialize one variable to point at the beginning of a list and a second variable/pointer to point at the end of list. We then shift the pointers to move inwards through the list towards each other, until our problem is solved or the pointers reach the opposite ends of the list.
"""
def is_palindrome(s):
    start = 0
    end = len(s) - 1
    while start < end :
        if s[start] == s[end] :
            start += 1
            end -= 1
        else:
            return False
    return True

s = "amanaplanacanalpanama"
s2 = "hello world"

print(is_palindrome(s))
print(is_palindrome(s2))
print()
"""
Problem 3: Evaluate Palindrome
The is_palindrome() problem can also be solved without using the two-pointer technique (as you may have seen it in previous units)! Evaluate the time and space complexity of your two-pointer solution.

Then, evaluate the time and space complexity of the following solution:

def is_palindrome(s):
    reverse = s[::-1]
    return reverse == s
Which has better time complexity?
Which has better space complexity?
"""
print('The two-pointer technique has better space complexity, while both methods have the same time complexity.')
print()

"""
Problem 4: Make Palindromes
You are given a string s consisting of lowercase English letters, and are allowed to perform operations on it. In one operation, you can replace a character in s with another lowercase English letter.

Write a function make_palindrome() that takes in a string s and turns it into a palindrome with the minimum number of operations as possible. If there are multiple palindromes that can be made using the minimum number of operations, make the lexicographically smallest one.

A string a is lexicographically smaller than a string b (of the same length) if in the first position where a and b differ, string a has a letter that appears earlier in the alphabet than the corresponding letter in b.

The function returns the resulting palindrome string.
"""        
def make_palindrome(s):
    s = list(s)  # Convert string to list to allow modification
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            if s[start] < s[end]:
                s[end] = s[start]  # Mirror the start character to the end
            else:
                s[start] = s[end]  # Mirror the end character to the start
        start += 1
        end -= 1
    
    return ''.join(s)  # Convert list back to string
    
s = "egcfe"
print(make_palindrome(s))
s = "abcd"
print(make_palindrome(s))
s = "seven"
print(make_palindrome(s))
print()

"""
Problem 5: Reverse Vowels
Write a function reverse_vowel() that takes in a string s as a parameter and returns a string with all the vowels in the string reversed. The consonants should remain in the same position. For this question, we consider a, e, i, o, and u as vowels but not y. The vowels can appear in both lower and upper cases, more than once.
"""
def reverse_vowels(s):
    s = list(s) # Convert string to list to allow modification
    vowels = ['a','e','i','o','u']
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] in vowels:
            while s[end] not in vowels and start < end:
                end -= 1
            s[start], s[end] = s[end], s[start]
            end -= 1
        start += 1
    
    return ''.join(s)
            
s1 = "hello"
rev_s1 = reverse_vowels(s1)
print(rev_s1)
s2 = "leetcode"
rev_s2 = reverse_vowels(s2)
print(rev_s2)
print()

"""
Problem 6: Two-Pointer Remove Element
The two-pointer approach can also be used with two pointers that iterate forward through a list or string at different rates. Use two pointers to solve the following problem:

Write a function removeElement() that takes in a list nums and a value val as parameters and removes all instances of that value in-place. The function returns the new length of nums.
"""
def removeElement(nums, val): 
    start = 0
    end = len(nums) - 1
    
    while start < end :
        if nums[start] in val :
            nums.remove(start)
            start += 1
    return nums
        
nums = [5, 4, 4, 3, 4, 1]
nums_len = removeElement(nums, 4)
print(nums) # same list
print(nums_len)
