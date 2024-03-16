# Date: 1/9/2024
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
# Add a new pizza to the original list
# Add a different pizza to the list friend_pizzas
# Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend's favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

# list of pizzas
pizzas = ['Mushroom', 'Pepperoni', 'Sausage']

# Copy of pizzas
friend_pizzas = pizzas[:]

# New list item in the pizzas list
pizzas.append('Bacon')
for pizza in pizzas:
    print(f'My favorite pizzas are: {pizza}')

# New list item in friend_pizzas list
friend_pizzas.append('Cheese')
for pizza in friend_pizzas:
    print(f'My friend\'s favorite pizzas are: {pizza}')