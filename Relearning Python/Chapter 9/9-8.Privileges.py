"""
Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
"""
class Admin():
    def __init__(self, privilege):
        """Initialize Admin's privileges"""
        self.privilege = ['Can delete post', 'Can ban user', 'Can add post']
        
    def show_privileges(self):
        """Print the Admin's power"""
        for i in self.privilege:
            print(f'- {i}')
            
Admin2 = Admin()
Admin2.show_privileges()