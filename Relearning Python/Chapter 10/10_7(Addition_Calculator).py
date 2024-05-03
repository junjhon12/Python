"""
Wrap your code from Exercise 10-5 in a while loop
so the user can continue entering numbers, even if they make a mistake and
enter text instead of a number.
"""

from pathlib import Path

path = Path("Relearning Python\Chapter 10\guest_book.txt")

added_name = input('Name:')
contents = (added_name)
while True:
    added_name = input('Name:')
    contents += ('\n'+added_name )
    if added_name == ('quit'):
        break
    if not added_name:
        added_name = input('Name:')
    path.write_text(contents)
print(path.read_text())