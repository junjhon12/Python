from pathlib import Path

path = Path("Relearning Python\Chapter 10\guest_book.txt")

added_name = input('Name:')
contents = (added_name)
while True:
    added_name = input('Name:')
    contents += ('\n'+added_name )
    if added_name == ('quit'):
        break
    path.write_text(contents)
print(path.read_text())