"""
The program file_reader.py in this section uses a temporary
variable, lines, to show how splitlines() works. You can skip the temporary
variable and loop directly over the list that splitlines() returns:
    for line in contents.splitlines():
Remove the temporary variable from each of the programs in this section,
to make them more concise.
"""
from pathlib import Path
path = Path('Relearning Python\Chapter 10\learning_python.txt')
contents = path.read_text()

for line in contents.splitlines():
    print(line)