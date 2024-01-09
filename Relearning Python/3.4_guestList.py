# Date: 1/ 1/ 2024
# Create a list of people to invite to dinner.
# Use your list to print a message to each person, inviting them to dinner.

# People list waiting ot be invited
people = ['personA', 'personB', 'personC']

# Print of first batch
print(f'Hey {people[0]} and {people[1]} come join me.\n{people[2]} hold on, let me change the table.')

# Remove those who have been seated
people.pop(0)
people.remove('personB')

# Print remaing list elements
print(people)

# Print second batch
print(f'Alright come on over {people[0]}.')

# Remove last person from list
people.pop(0)