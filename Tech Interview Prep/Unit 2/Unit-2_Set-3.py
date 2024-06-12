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
Write a function update_or_warn() that takes in a dictionary records, a key item, and a new value update_value as parameters. The function updates the value of item in records with update_value if item exists. If item does not exist, it should print "<item> not found!".
"""
def update_or_warn(records, item, update_value) :
    # Check if the item is inside the records dictionary
    if item in records :
        # Change the value of the found item with updated value
        print(f'"{item}" found, dictionary updated')
        records[item] = update_value
        print(records)
    else :
        print(f'"{item}" not found!')
    
records = {"apple": 1, "banana": 2, "orange": 3}
update_or_warn(records, "banana", 5)
update_or_warn(records, "grape", 4)
print()

"""
Write a function attendance_rate() that takes in a dictionary attendance_list as a parameter. The function maps student names to their attendance status ("Present" or "Absent"), and returns the percentage of students who are present.
"""
def attendance_rate(attendance_list) :
    
    count = 0
    # loop through attendance list items
    for i in attendance_list :
        # Check if the attendance's values equals Present
        if attendance_list[i] == "Present" :
            # Add the number of items meeting this condition
            count += 1
    # Return the percentage out of the whole that met the condition
    return ((count/len(attendance_list))*100)

attendance_list = {
    "Bluey": "Present", 
    "Bingo": "Absent", 
    "Snickers": "Present", 
    "Winton": "Absent"
}
print(attendance_rate(attendance_list))
print()

"""
Write a function average_book_ratings(), that calculates the average rating for each book in a collection. The function takes one parameter: a dictionary book_ratings where each key-value pair represents a book title and a list of its ratings, respectively. Ratings are represented as floating-point numbers. The function should return a new dictionary with book titles as keys and their average rating.
"""
def average_book_ratings(book_ratings):
    output = {}
    #return round(sum(book_ratings[i]) / len(book_ratings[i]), 1)
    for key, value in book_ratings.items() :
        output[key] = round(sum(value) / len(book_ratings), 1)
    return output
book_ratings = {
    "The Great Gatsby": [4.5, 3.0, 5.0],
    "To Kill a Mockingbird": [4.8, 5.0, 4.0, 4.9]
}
print(average_book_ratings(book_ratings))
print()

"""
Write a function odd_keys_even_values() that takes in dictionary as a parameter, a dictionary with integer keys and values. The function returns a list of keys that are odd where their corresponding values are even.
"""
def odd_keys_even_values(dictionary):
    output = []
    for key, values in dictionary.items() :
        if key % 2 != 0 and values % 2 == 0:
            output.append(key)
    return output
        
dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)
print()

"""
You're developing an analytics tool for a sports league. Your task is to write a function named team_with_best_average_score() that returns the team with the highest average score over a season.

The function should accept a list of dictionaries named games as a parameter. Each dictionary represents data from a game, including the "team_name", and the "score" they achieved in that game. The function calculates the average score for each team across all games and returns the team with the highest average score.
"""
def team_with_best_average_score(games):
    # ChatGPT answer
    output = {}

    for i in games:
        team_name = i['team_name']
        score = i['score']
        if team_name in output:
            output[team_name][0] += score
            output[team_name][1] += 1
        else:
            output[team_name] = [score, 1]

    return max(output, key=lambda team: output[team][0] / output[team][1])
    

games = [
    {"team_name": "Lions",
     "score": 23
    },
    {"team_name": "Tigers", 
     "score": 30
    },
    {"team_name": "Lions", 
     "score": 27
    },
    {"team_name": "Bears", 
     "score": 20
    },
    {"team_name": "Tigers", 
     "score": 24
    },
    {"team_name": "Bears", 
     "score": 22
    }
]
print(team_with_best_average_score(games))    
print()

"""
Write a function find_unique_items() that takes two lists list_a and list_b as parameters. Tje function identifies unique items from the lists and returns a dictionary with the items as keys and a boolean value as the value indicating whether the item is unique to the first list (True) or not (False).
""" 
def find_unique_items(list_a, list_b):
    output = {}
    for i in range(len(list_a)) :
        if list_a[i] not in list_b[i] :
            if list_a[i] in list_a[i] :
                output[list_a[i]] = True
            else :
                output[list_a[i]] = False
        if list_b[i] not in list_a[i] :
            if list_b[i] in list_a[i] :
                output[list_b[i]] = True
            else :
                output[list_b[i]] = False
    return output
            
    print(output)
list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
print(find_unique_items(list_a, list_b))