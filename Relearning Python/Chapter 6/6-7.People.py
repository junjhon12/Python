"""
6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). Make
two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through
the list, print everything you know about each person.
"""

person_A = {
    'First Name': 'FName A',
    'Last Name' : 'LName A',
    'Age': 15,
    'City': 'City A'
}

person_B = {
    'First Name': 'FName B',
    'Last Name' : 'LName B',
    'Age': 20,
    'City': 'City B'
}

person_C = {
    'First Name': 'FName C',
    'Last Name' : 'LName C',
    'Age': 25,
    'City': 'City C'
}

people = [person_A, person_B, person_C]

for people_info in people:
    print(people_info)