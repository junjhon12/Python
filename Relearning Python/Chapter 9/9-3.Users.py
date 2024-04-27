"""
Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.
"""

class User:
    def __init__(self, first_name, last_name, detail):
        """Initialize user's first name, last, and details about them"""
        self.fname = first_name
        self.lname = last_name
        self.detail = detail
        
    def describe_user(self):
        """Summary of the user's information"""
        print(f'{self.fname} {self.lname} has interest in {self.detail}')
        
    def greet_user(self):
        """Greet user"""
        print(f'Hello, {self.fname} {self.lname}')
        
user1 = User('Sung', 'Jin', 'light novel')
user1.describe_user()
user1.greet_user()

user1 = User('B', 'b', 'bbbbb')
user1.describe_user()
user1.greet_user()

user1 = User('C', 'c', 'ccccc')
user1.describe_user()
user1.greet_user()