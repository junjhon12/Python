"""
Problem 1: Sum of Strings
Write a function sum_of_number_strings() that takes in a list of strings nums. Each string is a representations of integers. The function should return the sum of these strings as an integer.
"""
def sum_of_number_strings(nums) :
    sum = 0
    for i in nums :
        sum += int(i)
    return sum
nums = ["10", "20", "30"]
sum = sum_of_number_strings(nums)
print(sum)
print()
"""
Problem 2: Remove Duplicates
Write a function remove_duplicates() that takes in a sorted list of integers nums as a parameter and removes all duplicates in the list. The function returns the modified list.
"""
def remove_duplicates(nums) :
    # Create an empty list
    no_dups = []
    # loop through the nums list
    for i in nums:
        # If the numberi sn't in the list add it in
        if i not in no_dups :
            no_dups.append(i)
            # If the number is already inside the no_dups list then go past the current i
        else:
            continue
    return no_dups
    
nums = [1,1,1,2,3,4,4,5,6,6]
print(remove_duplicates(nums))
print()
"""
Problem 3: Reverse Letters
Write a function reverse_only_letters() that takes in a string s as a parameter. The function reverses the order of the letters in the string and returns the new string. Non-letter characters should remain in their original positions.
"""
def reverse_only_letters(s):
    s_list = list(s)
    left, right = 0, len(s_list) - 1

    while left < right:
        if not s_list[left].isalpha():
            left += 1
        elif not s_list[right].isalpha():
            right -= 1
        else:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    return ''.join(s_list)

s = "a-bC-dEf-ghIj"
reversed_s = reverse_only_letters(s)
print(reversed_s)
print()
"""
Problem 4: Longest Uniform Substring
Write a function longest_uniform_substring() that takes in a string s and returns the length of the longest uniform substring. A uniform substring consists of a single repeated character.
"""
def longest_uniform_substring(s) :
    output = {}
    for i in s :
        output[i] = [s.count(i)]
    counts = output.values()
    return(max(counts))
s1 = "aabbbbCdAA"
l1 = longest_uniform_substring(s1)
print(l1)
s2 = "abcdef"
l2 = longest_uniform_substring(s2)
print(l2)
print()
"""
Problem 5: Teemo's Attack
In the game League of Legends, Teemo attacks his enemy Ashe with poison arrows. Write a function find_poisoned_duration() that takes in two parameters: time_series (the time at which Teemo's attacks hits Ashe) and time_duration (the duration of the poisoning effect). The function returns the total time that Ashe is in a poisoned condition.
time_series is a list of integers that represents the times at which Teemo attacks and makes Ashe poisoned for the exact time_duration.
If Teemo hits Ashe while she is still poisoned, the poison's duration starts over. For example, if Teemo attacks at times 1 and 4 for 3 seconds, the states at each time would be:
"""
def find_poisoned_duration(time_series, duration):
    last_num = int(time_series[-1])
    i = 1
    duration_left = duration
    count = 0
    while i <= last_num:
        if i == 1 :
            print(f"{i}: attack")
        elif i in time_series:
            print(f'{i}: attacked, poison duration resets to {duration}')
            duration_left = duration
        else :
            if duration_left <= 0 :
                print(f'{i}: in normal state')
            else:
                print(f'{i}: in poison state')
                count += 1
                last_num += 0.5
            duration_left -= 1
        i += 1
    return count
        
time_series = [1,4,9]
damage = find_poisoned_duration(time_series, 3)
print(damage)
print()

"""
Problem 6: Sum Unique Elements
Write a function sum_of_unique_elements() that takes in two lists of integers, lst1 and lst2, as parameters and returns the sum of the elements that are unique in lst1.

An element is unique if:

it appears exactly once in lst1
it does not appear in lst2
"""
def sum_of_unique_elements(lst1, lst2):
    # Use sets for faster lookup and operations
    set1 = set(lst1)
    set2 = set(lst2)
    # Initialize sum of unique elements
    sum_unique = 0
    # Iterate through elements in set1
    for num in set1:
        # Check if num appears exactly once in lst1 and does not appear in lst2
        if lst1.count(num) == 1 and num not in set2:
            sum_unique += num
    return sum_unique
            
        
lstA = [1, 2 ,3, 4] 
lstB = [3, 4, 5, 6]
lstC = [7, 7, 7, 7]

sum1 = sum_of_unique_elements(lstA, lstB)
print(sum1)
sum2 = sum_of_unique_elements(lstC, lstB)
print(sum1)

date = 'DD-MM-YYYY'
month = date[3:5]
print(month)