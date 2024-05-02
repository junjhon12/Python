"""
Read in each line from the file you just created, learning_python.txt, and
replace the word Python with the name of another language, such as C. Print
each modified line to the screen.
"""

from pathlib import Path

path = Path('Relearning Python\Chapter 10\learning_python.txt')
contents  = path.read_text()

for i in contents.splitlines():
    print(i.replace('Python', 'C'))