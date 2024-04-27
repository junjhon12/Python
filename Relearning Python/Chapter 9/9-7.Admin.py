"""
An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list of
strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
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
        
class Admin(User):
    def __init__(self, first_name, last_name, detail):
        """Initialize Admin's ability with User parent info"""
        super().__init__(first_name, last_name, detail)
        self.privilege = ['Can delete post', 'Can ban user', 'Can add post']
        
    def show_privileges(self):
        """Print the Admin's power"""
        print(f'{self.fname} {self.lname} privileges are:')
        for i in self.privilege:
            print(f'- {i}')
            
Admin1 = Admin('A', 'a', 'aaaa')
Admin1.show_privileges()