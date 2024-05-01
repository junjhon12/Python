class Admin():
    def __init__(self, privilege):
        """Initialize Admin's privileges"""
        self.privilege = ['Can delete post', 'Can ban user', 'Can add post']
        
    def show_privileges(self):
        """Print the Admin's power"""
        for i in self.privilege:
            print(f'- {i}')
            
            