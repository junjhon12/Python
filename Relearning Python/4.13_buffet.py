# Date: 1/9/2024   
# store five foods in a tuple
# Use for loop to print each food
# Modify one item and make sure Python rejects the change
# Add a line that rewrites tuple, and then use for loop to print each items on the revised list.

# food tuple
foods = ('Craw fish', 'Pizza', 'Sushie', 'Fries')

# print each food
for food in foods:
    print(food)
    
# Attempt to modify one item
# foods[4] = 'Chicken'

# Redefine tuple
foods = ('Craw fish', 'Pizza', 'Sushie', 'Fries', 'Chicken')
for food in foods:
    print(food)
