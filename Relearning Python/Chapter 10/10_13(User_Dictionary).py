from pathlib import Path
import json

def get_stored_user_info(path):
    """Get stored user information if available."""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None

def get_new_user_info(path):
    """Prompt for new user information."""
    username = input("What is your name? ")
    hobby = input(f"What's your hobby, {username}? ")
    interest = input(f"What's your interest, {username}? ")
    user_info = {'username': username, 'Hobby': hobby, 'Interest': interest}
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
    """Show the stored user information."""
    path = Path('username.json')
    user_info = get_stored_user_info(path)
    if user_info:
        print("\nUser Information:")
        for key, value in user_info.items():
            print(f"{key}: {value}")
    else:
        print("No user information found.")

# Greet the user and collect information
greet_user()

# Show the stored user information
show_user_info()
