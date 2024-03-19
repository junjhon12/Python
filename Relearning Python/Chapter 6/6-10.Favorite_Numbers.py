"""
Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
"""
favorite_number = {
    'person1': [1, 2],
    'person2': [2, 3],
    'person3': [3, 4],
    'person4': [4, 5],
    'person5': [5, 6]
}

for person, number in favorite_number.items():
    print(f'{person} favorite number is:')
    for numbers in number:
        print(f'\t{numbers}')