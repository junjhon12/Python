from pathlib import Path

path = Path('Relearning Python\Chapter 10\Guest.txt')
name = input("Enter your name: ")
path.write_text(name)
print(path.read_text())