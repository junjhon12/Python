"""
Store the User class in one module, and store the
Privileges and Admin classes in a separate module. In a separate file, create
an Admin instance and call show_privileges() to show that everything is still
working correctly.
"""
from User import *
from Admin_Privileges import *

admin1 = User('A', 'a', 'aaaa')
admin1 = Admin('')

admin1.show_privileges()
