"""
Visit Project Gutenberg (https://gutenberg.org) and find
a few texts you’d like to analyze. Download the text files for these works, or
copy the raw text from your browser into a text file on your computer.
You can use the count() method to find out how many times a word or
phrase appears in a string. For example, the following code counts the number
of times 'row' appears in a string:
"""
from pathlib import Path
path = Path('Relearning Python\Chapter 10\chapter10.txt')
class read_text:
    def __init__(self):
        pass
    def reading_text(self):
        while True:
            try:
                content = path.read_text()
            except FileNotFoundError:
                pass
            else:
                counted_text =  content.count('row')
                print(counted_text)
                counted_text = content.lower().count('row')
                print(counted_text)
                break
                
try1 = read_text()
try1.reading_text()