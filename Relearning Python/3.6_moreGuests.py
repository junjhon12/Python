# Date: 1/8/2024
# insert one guest to the beginning of the list
# insert one guest to the middle of the list
# insert one guest to the end of the list
# print second invite message, one for each person in your list

# People list
people = ['personA', 'personB', 'personC']

# Adding guest to the beginning of the list
people.insert(0, 'personD')
# Adding guest to the middle of the list
people.insert(2, 'personE')
# Adding guest to the end of the list
people.append('personF')

#Print second invite message for each person
print(f'{people[0]} is invited \n{people[1]} is invited \n{people[2]} is invited \n{people[3]} is invited \n{people[4]} is invited')