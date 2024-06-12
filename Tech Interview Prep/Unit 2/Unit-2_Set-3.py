"""
A mountain list is defined as a list that has at least three elements, where there exists some i with 0 < i < len(lst)-1 such that lst[0] < lst[1] < ... lst[i-1] < lst[i] and lst[i] > lst[i+1] > ... > lst[len(lst)-1].

Given such a mountain list lst as a parameter, write a function that finds and returns the highest peak (the index i of the maximum element).

Hint: This is a lists problem
"""
def peak_index_in_mountain_list(mountain_lst) :
    # for i in mountain_lst : print(i) = 0 3 8 0
    output = 0
    for i in mountain_lst :
        if i < mountain_lst[i-1] :
            return i-1
    
    
mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)
print()

"""
Write a function build_inventory() that takes in a list of product_names and a corresponding list of product_prices as parameters. The function returns a dictionary representing the inventory of a small store. Each product name in product_names should be a key in the dictionary and the corresponding value should be the item price.

product_names[i] should be paired with product_prices[i] in the dictionary where 0 <= i <= len(product_names). You may assume that product_names and product_prices are the same length.
"""
def build_inventory(product_names, product_prices) :
    output = {}
    
    for i in range(len(product_names)) :
        # Set output key as product_names items
        # Set output value as product_prices items
        output[product_names[i]] = product_prices[i]
    return output

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))
print()

"""

"""