import sqlite3

# Connect to the database
conn = sqlite3.connect('my_database.db')

# Create the tables if they don't exist
# Create a table named 'fish' with columns 'id', 'name', 'species', 'weight', 'length', and 'location'
conn.execute('''CREATE TABLE IF NOT EXISTS fish (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        species TEXT,
        weight REAL,
        length REAL,
        location TEXT
    )''')

# Table named 'catches' with columns 'id', 'fish_id', 'angler', 'date', and 'bait'
conn.execute('''CREATE TABLE IF NOT EXISTS catches (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fish_id INTEGER,
        angler TEXT,
        date TEXT,
        bait TEXT,
        FOREIGN KEY (fish_id) REFERENCES fish(id)
    )''')

# Function to add a fish to the database
def add_fish():
    # Get user input for the fish's name, species, weight, length, and location
    columns = ['name', 'species', 'weight', 'length', 'location']
    data = [input(f'Enter fish {col}: ') for col in columns]
    # Insert the fish data into the 'fish' table
    conn.execute(f"INSERT INTO fish (name, species, weight, length, location) VALUES (?, ?, ?, ?, ?)", data)
    conn.commit()
    print('Fish added successfully!')

# Function to remove a fish from the database
def remove_fish():
    # Get user input for the fish's ID
    fish_id = input('Enter fish ID: ')
    # Delete the fish with the given ID from the 'fish' table
    conn.execute(f"DELETE FROM fish WHERE id=?", (fish_id,))
    conn.commit()
    print('Fish removed successfully!')

# Function to print all fish in the database
def print_all_fish():
    # Select all rows from the 'fish' table and print them
    cursor = conn.execute("SELECT * FROM fish")
    for row in cursor:
        print(row)

# Function to print a specific fish from the database
def print_fish():
    # Get user input for the fish's ID
    fish_id = input('Enter fish ID: ')
    # Select the fish with the given ID from the 'fish' table and print it
    cursor = conn.execute("SELECT * FROM fish WHERE id=?", (fish_id,))
    print(cursor.fetchone())

# Function to update a fish in the database
def update_fish():
    # Get user input for the fish's ID and the columns to update
    fish_id = input('Enter fish ID: ')
    columns = ['name', 'species', 'weight', 'length', 'location']
    # Get user input for the new values of the columns to update
    updates = ', '.join([f"{col} = ?" for col in columns])
    data = [input(f'Enter new value for {col}: ') for col in columns]
    # Update the fish with the given ID in the 'fish' table with the new values
    query = f"UPDATE fish SET {updates} WHERE id=?"
    conn.execute(query, (*data, fish_id))
    conn.commit()
    print('Fish updated successfully!')

# Function to add a catch to the database
def add_catch():
    # Get user input for the catch's fish ID, angler, date, and bait
    columns = ['fish_id', 'angler', 'date', 'bait']
    data = [input(f'Enter catch {col}: ') for col in columns]
    # Insert the catch data into the 'catches' table
    conn.execute(f"INSERT INTO catches (fish_id, angler, date, bait) VALUES (?, ?, ?, ?)", data)
    conn.commit()
    print('Catch added successfully!')

# Function to remove a catch from the database
def remove_catch():
    # Get user input for the catch's ID
    catch_id = input('Enter catch ID: ')
    # Delete the catch with the given ID from the 'catches' table
    conn.execute(f"DELETE FROM catches WHERE id=?", (catch_id,))
    conn.commit()
    print('Catch removed successfully!')

# Function to print all catches in the database
def print_all_catches():
    # Select all rows from the 'catches' table and print them
    cursor = conn.execute("SELECT * FROM catches")
    for row in cursor:
        print(row)

# Function to print a specific catch from the database
def print_catch():
    # Get user input for the catch's ID
    catch_id = input('Enter catch ID: ')
    # Select the catch with the given ID from the 'catches' table and print it
    cursor = conn.execute("SELECT * FROM catches WHERE id=?", (catch_id,))
    print(cursor.fetchone())

# Function to update a catch in the database
def update_catch():
    # Get user input for the catch's ID and the columns to update
    catch_id = input('Enter catch ID: ')
    columns = ['fish_id', 'angler', 'date', 'bait']
    # Get user input for the new values of the columns to update
    updates = ', '.join([f"{col} = ?" for col in columns])
    data = [input(f'Enter new value for {col}: ') for col in columns]
    # Update the catch with the given ID in the 'catches' table with the new values
    query = f"UPDATE catches SET {updates} WHERE id=?"
    conn.execute(query, (*data, catch_id))
    conn.commit()
    print('Catch updated successfully!')

# Main loop
while True:
    # Get user input for the command to execute
    command = input('Enter a command: ')
    # Execute the corresponding function based on the command
        #Fishes
    if command.lower() == 'add fish':
        add_fish()
    elif command.lower() == 'remove fish':
        remove_fish()
    elif command.lower() == 'print all fish':
        print_all_fish()
    elif command.lower() == 'print fish':
        print_fish()
    elif command.lower() == 'update fish':
        update_fish()
        #Catches
    elif command.lower() == 'add catch':
        add_catch()
    elif command.lower() == 'remove catch':
        remove_catch()
    elif command.lower() == 'print all catches':
        print_all_catches()
    elif command.lower() == 'print catch':
        print_catch()
    elif command.lower() == 'update catch':
        update_catch()
    elif command.lower() in ['quit', 'q']:
        break
    else:
        print('Invalid command. Please try again.')

# Close the database connection
conn.close()
