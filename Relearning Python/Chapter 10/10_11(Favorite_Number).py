"""
Write a program that prompts for the user’s favorite
number. Use json.dumps() to store this number in a file. Write a separate program that reads in this value and prints the message “I know your favorite
number! It’s _____.
"""

from pathlib import Path
import json

class favorite_number:
    
    def __init__(self):
       self. path = Path('fav_number.json')
    
    def get_number(self):
        while True:
            try: 
                get_number = input('Enter your favorite number: ')
                if get_number == 'quit':
                    break
                fav_number = int(get_number)
                fav_number_json = json.dumps(fav_number)
                self.path.write_text(fav_number_json)
            except ValueError:
                print('Enter a valid number')
            else:
                break     
            
    def print_number(self):
        while True:
            try:
                fav_nunber_json = self.path.read_text()
                fav_number = json.loads(fav_nunber_json)
                print(f'I know your favorite number! It’s {fav_number}.')
            except BufferError:
                print('Could not be run')
            else:
                break
        
num1 = favorite_number()
num1.get_number()
num1.print_number()