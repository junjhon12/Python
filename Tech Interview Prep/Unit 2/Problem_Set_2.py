"""
Problem 1: Is Monotonic
Write a function is_monotonic() that takes in a list nums as a parameter and checks if it is either monotone increasing or monotone decreasing.
A list is monotone increasing if every element is either greater than or equal to the element before it.
A list is monotone decreasing if every element is either less than or equal to the element before it.
The function should return True if the given list is either monotone increasing or decreasing and False otherwise.
Hint: This is a lists problem
"""

def is_monotonic(nums):
    increasing = decreasing = True

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            decreasing = False
        if nums[i] < nums[i - 1]:
            increasing = False

    return increasing or decreasing
        
nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))
print()

"""
Problem 2: Student Directory
Write a function student_directory() that takes a list of student_names as a parameter and returns a dictionary of students, where each student in student_names is a key mapped to a unique numerical student ID.
Example Input: student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
Example Output: {"Ada Lovelace": 1, "Tu Youyou": 2, "Mae Jemison": 3, "Rajeshwari Chatterjee": 4, "Alan Turing": 
"""

def student_directory(student_names) :
    # Init new dictionary
    output = {}
    # Loop through the student_name's elements
    for i in range(len(student_names)) :
        #Student name is key while the value is +1 psoition, Key:Value
        output[student_names[i]] = i+1
    return output
student_names = ["Ada Lovelace", "Tu Youyou", "Mae Jemison", "Rajeshwari Chatterjee", "Alan Turing"]
print(student_directory(student_names))
print()

"""
The following function get_description() takes in a dictionary info and a list keys as parameters. For each key in keys, the function prints the value associated with that key in info and prints None if the key does not exist in info.
"""
def get_description(info, keys):
    #print(info.get('name')) tom
    '''
    I did this
    output = {}
    for key in keys:
        if key in info:
            print(f"{key} : " + info[key])
        elif key not in info :
            print(f"{key} : None")
    '''        
    # or just do this
    for key in keys:
        print(f"{key} : {info.get(key)}")
            
info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)
print()

"""
Write a function sum_even_values() that returns the sum of all even values in a given dictionary. Assume the dictionary values are all integers.
"""
def sum_even_values(dictionary) :
    sum = 0
    # loop through each dictionary's items
    for i in dictionary :
        # Check if the dictionary's value are EVEN
        if dictionary[i] % 2 == 0 :
            # Add the value to sum
            sum += dictionary[i]
    return sum
dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))
print()

"""
Write a function merge_catalogs() that combines two product catalogs, catalog1 and catalog2 as parameters. Each parameter is a dictionary where each key-value pair represents a product name and its price, respectively. If the same product exists in both catalogs, the price from the second catalog should overwrite the price in the first. Return the updated first catalog dictionary.
"""
def merge_catalogs(catalog1, catalog2) :
    # loop through catalog2 dictionary
    for i in catalog2 :
        # Check if catalog2 and catalog1 have the same items
        if i in catalog1 :
            # Cchange the value of catalog1's item if catalog2's item value is higher
            if catalog2[i] > catalog1[i] :
                catalog1[i] = catalog2[i]
            return catalog1

catalog1 = {"apple": 1.0, "banana": 0.5}
catalog2 = {"banana": 0.75, "cherry": 1.25}
print(merge_catalogs(catalog1, catalog2))
print()

"""
Write a function get_items_to_restock() that takes in a dictionary products that maps product names to their quantities and an integer restock_threshold as parameters. The function returns a list of products that have a value less than restock_threshold and need to be restocked. If products is empty, the function return an empty list.
"""
def get_items_to_restock(products, restock_threshold) :
    # print(products[i]) 10, 2, 5, 3
    # print(i) Product1m Product2, ...
    """
    output = {}
    for i in products :
        if products[i] < restock_threshold:
            output[i] = products.get(i)
    return output
    """
    #Answer
    # Empty List
    output = []
    for i in products :
        if products[i] < restock_threshold:
            output.append(i)
    return output
    
products = {"Product1": 10, "Product2": 2, "Product3": 5, "Product4": 3}
restock_threshold = 5
print(get_items_to_restock(products, restock_threshold)) 
print()