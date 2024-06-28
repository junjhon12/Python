"""
Problem 1: Pokemon Class
Step 1: Copy the following code into Replit.

Step 2: Add a line of code (outside of the class) to instantiate an instance of the class Pokemon and store it in a variable named my_pokemon. The Pokemon instance created should have name "Pikachu" and its types should be ["Electric"].
"""
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

# Created a variable called my_pokemon to instantiate class Pokemon
my_pokemon = Pokemon("Pikachu", ["Electric"])
print()
"""
Problem 2: Create Squirtle
Step 1: Add the print_pokemon definition below to your code on Replit.

Step 2: Instantiate an instance of the class Pokemon and store it in a variable named squirtle. The Pokemon instance created should have name "Squirtle" and its types should be ["Water"].

Step 3: Call the method print_pokemon() on your new Pokemon instance squirtle.
"""
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
my_pokemon2 = Pokemon("Squirtle", ["Water"])
my_pokemon2.print_pokemon() #Prints using the print_pokemon function
print()

"""
Problem 3: Is Caught
Using your code from Problem 2, update your squirtle Pokemon so that is_caught is updated to True. Use the print_pokemon() function to verify that squirtle's is_caught property was updated.
"""
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
        
my_pokemon2.is_caught = True
my_pokemon2.print_pokemon()
print()

"""
Problem 4: Catch Pokemon
Update the Pokemon class with a new method catch() that takes in no parameters except self.

The method should update the Pokemon's is_caught attribute to True and not return any value.
"""
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
        
    def catch(self):
        self.is_caught = True
        
    def choose(self):
        if self.is_caught == True :
            print(f"{self.name} I choose you!") 
        else :
            print(f"{self.name} is wild! Catch them if you can!")
        
my_pokemon = Pokemon("rattata", ["Normal"])
my_pokemon.print_pokemon()

my_pokemon.choose()
my_pokemon.catch()
my_pokemon.choose()
print()

"""
Problem 6: Add Pokemon Type
Update the Pokemon class with a new method add_type() that takes in a string new_type as a parameter.

It should add new_type to the Pokemon's list of types.
"""
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
        
    def catch(self):
        self.is_caught = True
        
    def choose(self):
        if self.is_caught == True :
            print(f"{self.name} I choose you!") 
        else :
            print(f"{self.name} is wild! Catch them if you can!")
            
    def add_type(self, new_type) :
        self.types = list(self.types)
        self.types.append(new_type)
        
jigglypuff = Pokemon("Jigglypuff", ["Normal"])
jigglypuff.print_pokemon()

jigglypuff.add_type("Fairy")
jigglypuff.print_pokemon()
print()
"""
Problem 7: Get Pokemon
Outside the Pokemon class, write a new function get_by_type() that takes in a list of Pokemon instances my_pokemon and a string pokemon_type as parameters.

The function should return a list of all Pokemon instances from my_pokemon that have the type pokemon_type.
"""
class Pokemon:
    def __init__(self, name, types):
        self.name = name
        self.types = types
        self.is_caught = False

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
        
    def catch(self):
        self.is_caught = True
        
    def choose(self):
        if self.is_caught == True :
            print(f"{self.name} I choose you!") 
        else :
            print(f"{self.name} is wild! Catch them if you can!")
            
    def add_type(self, new_type) :
        self.types = list(self.types)
        self.types.append(new_type)
        
    def get_by_type(my_pokemon, pokemon_type):
        output = []
        for pokemon in my_pokemon :
            if pokemon_type in pokemon.types :
                output.append(pokemon.name)
        return output
        
jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
diglett = Pokemon("Diglett", ["Ground"])
meowth = Pokemon("Meowth", ["Normal"])
pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
blastoise = Pokemon("Blastoise", ["Water"])

my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
normal_pokemon = Pokemon.get_by_type(my_pokemon, "Normal")
print(normal_pokemon)
print()

"""
Problem 8: Pokemon Evolution
Some Pokemon can evolve into other species of Pokemon. In the updated Pokemon class below, each instance of Pokemon has an attribute evolution. The attribute will either be the default value of None or another Pokemon instance.

Write a function get_evolutionary_line() that takes in a Pokemon object starter_pokemon as a parameter.

The function should return a list of itself and the Pokemon that the starter_pokemon can evolve into.
"""
class Pokemon:
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution

    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
        
    def catch(self):
        self.is_caught = True
        
    def choose(self):
        if self.is_caught == True :
            print(f"{self.name} I choose you!") 
        else :
            print(f"{self.name} is wild! Catch them if you can!")
            
    def add_type(self, new_type) :
        self.types = list(self.types)
        self.types.append(new_type)
        
    def get_by_type(my_pokemon, pokemon_type):
        output = []
        for pokemon in my_pokemon :
            if pokemon_type in pokemon.types :
                output.append(pokemon.name)
        return output
    
    def get_evolutionary_line(starter_pokemon):
        output = []
        while starter_pokemon:
            output.append(starter_pokemon.name)
            starter_pokemon = starter_pokemon.evolution
        return output
        
charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = Pokemon.get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = Pokemon.get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = Pokemon.get_evolutionary_line(charizard)
print(charizard_list)
print()

"""
Problem 9: Node Class
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class below, create two nodes:

The first node should have value a and be stored in a variable node_one.
The second node should have value b and be stored in a variable node_two.
You do not need to connect the nodes together yet.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
  
node_one = Node('a')
node_two = Node('b')
  
print(node_one.value) 
print(node_one.next) 
print(node_two.value)
print(node_two.next) 
print()

"""
Problem 11: Mario Party
Create the list ["Mario", "Luigi", "Wario", "Toad"] as a linked list given the Node class:
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
list = ["Mario", "Luigi", "Wario", "Toad"]
node_4 = Node(list[3])
node_3 = Node(list[2], node_4)
node_2 = Node(list[1], node_3)
node_1 = Node(list[0], node_2)

print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next.value)
print(node_3.value, "->", node_3.next.value)
print(node_4.value, "->", node_4.next)
print()
"""
Problem 12: Printing Linked List
Write a function print_linked_list() that takes in a head node as a parameter and prints the linked list using the string " -> " to separate each node.

Note: The "head" of a linked list is the first element in the linked list, equivalent to lst[0] of a normal list.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next= next
		
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print()
    
node_e = Node('e')
node_d = Node('d', node_e)
node_c = Node('c', node_d)
node_b = Node('b', node_c)
node_a = Node('a', node_b)
print_linked_list(node_a)
print("==============================================================================================")

class Card():
    def  __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
  
    def print_card(self):
        print(f"{self.rank} of {self.suit}")
        
    def is_valid(self) :
        valid_suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
        valid_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
        if self.suit in valid_suits and self.rank in valid_ranks :
            return True
        return False
    
    def get_value(self) :
        value = 0
        num_ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10"]
        if self.rank in num_ranks :
            value = int(card.rank)
            return value
        elif self.rank == "Ace" :
            return 1
        elif self.rank == "Jack" :
            return 11
        elif self.rank == "Queen" :
            return 12
        elif self.rank == "King" :
            return 13
        else:
            return None
class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)
        pass

    def remove_card(self, card):
        if card in self.cards :
            self.cards.remove(card)
        pass
"""
Problem 1: Card Class
Step 1: Copy the following code into Replit.

Step 2: Instantiate an instance of the class Card and store it in a variable named card. The Card object should have the suit "Spades" and the rank "8".
"""
card = Card("Spades", 8)
"""
Problem 2: Print Card
Step 1: Update the Card class with the new method print_card() provided below:

def print_card(self):
	print(f"{self.rank} of {self.suit}")
Step 2: Create an instance of the class and store it in a variable named card. The object should have suit "Clubs" and rank "Ace".

Step 3: Then, call the method print_card() on your card.

Expected Output: Ace of Clubs
"""
card.suit = "Clubs"
card.rank = "Ace"
card.print_card()
print()
"""
Problem 3: Verify Update
Step 1: Using the same Card class from Problem 2, update your code so that the suit of card is "Hearts" instead of "Clubs".

Step 2: Use the print_card() method to verify that card was updated.

Expected Output: Ace of Hearts
"""
card.suit = "Hearts"
card.print_card()
print()
"""
Problem 4: Valid Card
Update the Card class with a new method is_valid() that takes in no parameters except self. The method should return True if:

The suit is one of the following values: "Hearts", "Spades", "Clubs", "Diamonds"
The rank is one of the following values: "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"
Otherwise, the method should return False
"""
my_card = Card("Hearts", "7")
print(my_card.is_valid())
second_draw = Card("Spades", "Joker")
print(second_draw.is_valid())
print()
"""
Problem 5: Get Value
Update the Card class with a new method get_value() that takes in no parameters except self.

The function returns the card's value depending on the card's rank:

If the card has rank 2, 3, 4, 5, 6, 7, 8, 9, 10, the method should return the rank as an integer
If the card has rank Ace, the method should return 1 as the card's value
If the card has rank Jack, the method should return 11 as the card's value
If the card has rank Queen, the method should return 12 as the card's value
If the card has rank King, the method should return 13 as the card's value
If the card is invalid, the method should return None
"""
card = Card("Hearts", "7")
print(card.get_value())
card_two = Card("Spades", "Jack")
print(card_two.get_value())
print()
"""
Problem 6: Hand Class
Step 1: Add the following Hand class to your code that represents a player's hand of cards.

A new instance of Hand is always empty.
Step 2: Add two methods add_card() and remove_card() to the Hand class that each accept a Card object as a parameter.

add_card() should add the Card to the player's Hand
remove_card() should remove the card from the player's Hand.
"""
card_one = Card("Hearts", "3")
card_two = Card("Spades", "8")

player1_hand = Hand()
# cards = []

player1_hand.add_card(card_one)
# cards = [card_one]

player1_hand.add_card(card_two)
# cards = [card_one, card_two]

player1_hand.remove_card(card_one)
# cards = [card_two]