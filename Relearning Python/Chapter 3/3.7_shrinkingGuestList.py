# Date: 1/8/2024
# Use pop() to remove guests until only two remain
# Print a message to the remaining two, letting them know they're still invited
# Use del to remove the last two names from the list, so you have an empty list

# People list
people = ['personD', 'personA', 'personE', 'personB', 'personC', 'personF']

# Pop guests until two remain
people.pop(0) 
print(f'sorry, you\'re no longer invited personD')
people.pop(1)
print(f'sorry, you\'re no longer invited personE')
people.pop(2)
print(f'sorry, you\'re no longer invited personC')
people.pop(2)
print(f'sorry, you\'re no longer invited personF')

# Print message to remaining two
print(f'You\'re still invited {people[0]}')
print(f'You\'re still invited {people[1]}')
print(people)

# Delete last two names from list
del people[0]
del people[0]
print(people)