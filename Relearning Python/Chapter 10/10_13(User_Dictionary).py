"""
The remember_me.py example only stores one piece of
information, the username. Expand this example by asking for two more pieces
of information about the user, then store all the information you collect in a
dictionary. Write this dictionary to a file using json.dumps(), and read it back
in using json.loads(). Print a summary showing exactly what your program
remembers about the user.
"""

from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """Prompt for a new user information."""
    username = input("What is your name?")
    hobby = input(f"What's your hobby {username}? ")
    interest = input(f"What's your interest {username}? ")
    user_info = {
        'username':username,
        'Hobby':hobby,
        'Interest':interest 
    }
    contents = json.dumps(user_info)
    path.write_text(contents)
    return user_info
    
def greet_user():
    """Greet the user by name."""
    path = Path('username.json')
    user_info = get_stored_user_info(path)
    if user_info:
        print(f'Welcome back, {user_info["username"]}!')
    else:
        user_info = get_new_user_info(path)
        print(f"We'll remember you when you come back, {user_info['username']}!")
        
def show_user_info():
    """Shpw stored user info"""
    path = Path('username.json')
    user_info = get_stored_user_info(path)
    if user_info:
        for key, value in user_info.items():
            print(f'{key}, {value}')
        else:
            print("No Info")
            
greet_user()
show_user_info()
