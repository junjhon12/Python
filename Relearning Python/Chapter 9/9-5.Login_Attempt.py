"""
Add an attribute called login_attempts to your User class
from Exercise 9-3 (page 162). Write a method called increment_login_attempts()
that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0
"""

class User:
    def __init__(self, first_name, last_name, detail):
        """Initialize user's first name, last, and details about them"""
        self.fname = first_name
        self.lname = last_name
        self.detail = detail
        self.login_attempts = 0
        
    def describe_user(self):
        """Summary of the user's information"""
        print(f'{self.fname} {self.lname} has interest in {self.detail}')
        
    def greet_user(self):
        """Greet user"""
        print(f'Hello, {self.fname} {self.lname}')
        
    def increment_login_attempts(self):
        """Add 1 additional to login attempts"""
        self.login_attempts += 1
        print(f'Number of attempts : {self.login_attempts}')
        
    def reset_login_attempts(self):
        """Reset login attempts"""
        self.login_attempts = 0
        print(f'Attempts is now back to {self.login_attempts}')
        
user1 = User('A', 'a', 'aaa')
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()