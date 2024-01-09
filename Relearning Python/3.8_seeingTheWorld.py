# Date: 1/8/2024

# Store locations in a list, not in order
location = ['B', 'A', 'C']

# Print list
print(location)

# Use sorted() to print list in alphabetical order without modifying the list
print(sorted(location))

# Use sorted() to print list in reverse alphabetical order without modifying the list
print(sorted(location, reverse=True))

# Use reverse() to change the order of the list
location.reverse()
print(location)

# Use sort() to change the order of the list alphabetically
location.sort()
print(location)

# Use sort() to change the order of the list reverse alphabetically
location.sort(reverse=True)
print(location)

