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
        pass # Fail Silently

    try:
        with open(dogs_file) as file:
            print("Contents of dogs.txt:")
            print(file.read())
    except FileNotFoundError:
        pass # Fail Silently

# Create the files and write data to them
create_files()

# Read and print the contents of the files
read_files()
