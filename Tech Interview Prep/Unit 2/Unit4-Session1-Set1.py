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
    
    # Pointer j for the position of the next unique element
    j = 1
    
    # Iterate through the array with i
    for i in range(1, len(nums)):
        if nums[i] != nums[i-1]:
            nums[j] = nums[i]
            j += 1
    return j  # The new length after removing duplicates
        
            
nums = [1,1,2,3,4,4,4,5]
print(nums)
print(remove_duplicates(nums))
print(nums) # same list