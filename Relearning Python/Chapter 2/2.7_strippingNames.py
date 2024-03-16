# Date: 12/29/2023
# Use a variable for person's name and include whitespace characters a the start and end of the name.
# Make sure you use each character combination, "\t" and "\n", at least once.
# Print name once, so the whitespace around the name is displayed.
# Then print name using each of the three stripping functions, lstrip(), rstrip(), and strip().

name = " \n\tJack\t Reynolds "
print(name.lstrip())
print(name.rstrip())
print(name.strip())