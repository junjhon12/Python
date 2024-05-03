"""
Make two files, cats.txt and dogs.txt. Store at least three
names of cats in the first file and three names of dogs in the second file. Write
a program that tries to read these files and print the contents of the file to the
screen. Wrap your code in a try-except block to catch the FileNotFound error,
and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block
executes properly.
"""

from pathlib import Path

def create_files():
    # Define the file paths
    cats_file = Path('cats.txt')
    dogs_file = Path('dogs.txt')

    # Write data to the files
    with open(cats_file, 'w') as file:
        file.write("Whiskers\n")
        file.write("Mittens\n")
        file.write("Snowball\n")

    with open(dogs_file, 'w') as file:
        file.write("Buddy\n")
        file.write("Max\n")
        file.write("Charlie\n")

def read_files():
    # Define the file paths
    cats_file = Path('cats.txt')
    dogs_file = Path('dogs.txt')

    # Read and print the contents of the files
    try:
        with open(cats_file) as file:
            print("Contents of cats.txt:")
            print(file.read())
    except FileNotFoundError:
        print(f'{cats_file} was not found.')

    try:
        with open(dogs_file) as file:
            print("Contents of dogs.txt:")
            print(file.read())
    except FileNotFoundError:
        print(f'{dogs_file} was not found.')

# Create the files and write data to them
create_files()

# Read and print the contents of the files
read_files()
