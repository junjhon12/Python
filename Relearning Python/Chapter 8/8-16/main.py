import function1
function1.make_pizza(20, 'meat1', 'meat2', 'meat3')

from function2 import build_profile
print(build_profile('Quoc', 'Le', focus='CS', interest='manga'))

from function3 import greet_users as greet
greet('Name1')

import function1 as pizza
pizza.make_pizza(14, 'stuff1')

from function2 import * #import every function from the module
print(build_profile('Quoc', 'Le', focus='CS', interest='manga'))
