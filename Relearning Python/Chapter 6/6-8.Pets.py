"""
Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets. Next, loop through your list and as
you do, print everything you know about each pet
"""

pet_A = {
    'Animal': 'Chicken',
    'Owner Name': 'Owner A'
}
    
pet_B = {
    'Animal': 'Fish',
    'Owner Name': 'Owner B'
}

pet_C = {
    'Animal': 'Dog',
    'Owner Name': 'Owner C'
}

pets = [pet_A, pet_B, pet_C]

for owner_info in pets:
    print(owner_info)