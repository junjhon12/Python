"""
Open a blank file in your text editor and write a few lines
summarizing what you’ve learned about Python so far. Start each line with the
phrase In Python you can. . . . Save the file as learning_python.txt in the same
directory as your exercises from this chapter. Write a program that reads the file
and prints what you wrote two times: print the contents once by reading in the
entire file, and once by storing the lines in a list and then looping over each line
"""
from pathlib import Path

path = Path('Relearning Python\Chapter 10\learning_python.txt')
contents = path.read_text().rstrip()
print(contents)
print()

for i in contents.splitlines():
    print(i)