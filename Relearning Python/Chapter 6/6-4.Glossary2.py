"""
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 99) by replacing your series of print()
calls with a loop that runs through the dictionary’s keys and values. When
you’re sure that your loop works, add five more Python terms to your glossary.
When you run your program again, these new words and meanings should
automatically be included in the output.
"""

Glossary = {
    'Dictionary': 'a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. ',
    'key-value pair': 'a set of values associated with each other. When you provide a key, Python returns the value associated with that key. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.',
    'Tuples': 'values that cannot change as immutable, and an immutable list',
    'constants': 'a variable whose value stays the same throughout the life of a program.',
    'comment': 'write notes in your spoken language, within your programs.'
}

for word,definition in Glossary.items():
    print(f'{word} : {definition}')