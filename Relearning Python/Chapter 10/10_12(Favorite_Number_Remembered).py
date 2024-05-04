"""
Combine the two programs you wrote in Exercise 10-11 into one file.
If the number is already stored, report the favorite number to the user. 
If not, prompt for the user’s favorite number and store it in a file.
Run the program twice to see that it works
"""
from pathlib import Path
import json

class favorite_number_remember:
    def __init__(self):
        self. path = Path('fav_number.json')
    
    def favorite_number(self):
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
            except BufferError:
                print('Could not be run')
            else:
                print(f'I know your favorite number! It’s {fav_number}.')
                break
            
num1 = favorite_number_remember()
num1.favorite_number()