# Date: 1/ 1/ 2024
# Print all guests who can't make it
# Modify the list of those who can't make it with new person you're inviting
# Print second invite message, one for each person in your list

# People list waiting ot be invited
people = ['personA', 'personB', 'personC']

# Print name of guest that can't make it
print(f'{people[1]} won\'t be able to attend.')

# Replace the guest that won't make it
people.remove('personB')
people.append('personD') # Added to the end of the list
# Print new guest
print(f'Therefore, {people[2]} will taking their place.')

# Second invite message
print(f'{people[0]} is invited \n{people[1]} is invited \n{people[2]} is invited')