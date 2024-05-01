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