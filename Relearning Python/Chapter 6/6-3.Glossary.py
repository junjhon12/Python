"""
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let's call it a glossary.
• Think of five programming words you've learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
"""

Glossary = {
    'Dictionary': 'a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. ',
    'key-value pair': 'a set of values associated with each other. When you provide a key, Python returns the value associated with that key. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas.',
    'Tuples': 'values that cannot change as immutable, and an immutable list',
    'constants': 'a variable whose value stays the same throughout the life of a program.',
    'comment': 'write notes in your spoken language, within your programs.'
}

print(f"Dictionary, {Glossary['Dictionary']}")
print(f"Key-value pair, {Glossary['key-value pair']}")
print(f"Tuples, {Glossary['Tuples']}")
print(f"Constants, {Glossary['constants']}")
print(f"Comment, {Glossary['comment']}")