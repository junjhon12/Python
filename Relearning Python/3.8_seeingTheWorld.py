# Date: 1/8/2024
# Store locations in a list, not in order
# Print list
# Use sorted() to print list in alphabetical order without modifying the list
# Use sorted() to print list in reverse alphabetical order without modifying the list
# Use reverse() to change the order of the list
# USe sort() to change the order of the list permanently
# Use sort() to change your list so it's stored in reverse alphabetical order

locations = ['Paris', 'London', 'New York', 'Tokyo', 'Sydney']
print(locations)
print(sorted(locations)) # Temporarily sorted
print(sorted(locations, reverse=True)) # Temporarily sorted in reverse
locations.reverse() # Permanently reversed
print(locations) # Permanently reversed
locations.sort() # Permanently sorted
print(locations) # Permanently sorted
locations.sort(reverse=True) # Permanently sorted in reverse
print(locations) # Permanently sorted in reverse
