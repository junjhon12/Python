"""
Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time
"""
def make_sandwhich(*demands):
    print(f"You wanted {len(demands)} things in your sandwhich:")
    for i in demands:
        print(f"- {i}")
        
make_sandwhich('meat1', 'meat2', 'meat3')