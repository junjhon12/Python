class Pokemon():
    def  __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp # hit points
        self.damage = damage # The amount of damage this pokemon does to its opponent every attack

    def attack(self, opponent):
        if self.damage > opponent.hp :
            return f"{opponent} fainted"
        else :
            opponent.hp -= self.damage
            print(f'{self.name} dealt {self.damage} to {opponent.name}')
"""
Problem 1: Battle Pokemon
Given the Pokemon class below, copy the code and add it to your Replit.
Then, write a method attack() that takes in a Pokemon object opponent and decreases opponent's hp by their self's damage amount.

If damaging the opponent leads to the opponent having an hp of 0 or less, the function should set the opponent's hp to 0 and print out "<Opponent name> fainted>.

Otherwise, the function should print out "<Pokemon name> dealt <damage> damage to <opponent name>".
"""
pikachu = Pokemon("Pikachu", 35, 20)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 
opponent = bulbasaur
pikachu.attack(opponent)
print()
"""
Problem 2: Convert to Linked List
A linked list is a new data type that, similar to a normal list or array, allows us to store pieces of data sequentially. The difference between a linked list and a normal list lies in how each element is stored in a computer’s memory.

In a normal list, individual elements of the list are stored in adjacent memory locations according to the order they appear in the list. If we know where the first element of the list is stored, it’s really easy to find any other element in the list.

In a linked list, the individual elements called nodes are not stored in sequential memory locations. Each node may be stored in an unrelated memory location. To connect nodes together into a sequential list, each node stores a reference or pointer to the next node in the list.

Using the provided Node class below, create the normal Python list ["Jigglypuff", "Wigglytuff"] as a linked list.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
list_2 = ["Jigglypuff", "Wigglytuff"]
node_2 = Node(list_2[1])
node_1 = Node(list_2[0], node_2)
print(node_1.value, "->", node_1.next.value)
print(node_2.value, "->", node_2.next)
print()
"""
Problem 3: Add First
Write a function add_first() that takes in a head of a linked list and a new_node from the Node class as parameters.

It should insert new_node as the new head of the linked_list. The function returns new_node.

Note: The "head" of a linked list is the first element in the linked list. Equivalent to lst[0] of a normal list.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
		
def add_first(head, new_node):
    new_node.next = head
    return new_node
    
print(node_1.value, "->", node_1.next.value)
new_node = Node("Ditto")
node_1 = add_first(node_1, new_node)
print(node_1.value, "->", node_1.next.value)
print()
"""
Problem 4: Get Tail
Write a function get_tail() that takes in the head of a linked list as a parameter.

It should print out the value of the tail of the list.

If the list is empty (head is None), return None.
Note: The "tail" of a list is the last element in the linked list. Equivalent to lst[-1] in a normal list.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def get_tail(head):
    if head is None:
        return None
    current = head
    # Traverse the list until the end is reached
    while current.next:
        current = current.next
    # Return the value of the last node
    return current.value
    
num3 = Node(3)
num2 = Node(2, num3)
num1 = Node(1, num2)
    
head = num1
tail = get_tail(num1)
print(tail)
"""
Problem 5: Replace Node
Using the Node class, write a function ll_replace() that takes a head of a linked list and two values, original and replacement as parameters.

The function updates any node with value original to have value replacement.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_replace(head, original, replacement):
    current = head
    # Loop through if there is a current
    while current:
        # Check if the current value is the original
        if current.value == original:
            # Replace the value to the replacement
            current.value = replacement
        print(current.value, end="")
        if current.next:
            print(" -> ", end="")
        current = current.next
    print()
    
num3 = Node(5)
num2 = Node(6, num3)
num1 = Node(5, num2)
# initial linked list: 5 -> 6 -> 5

head = num1
ll_replace(head, 5, "banana")
# updated linked list: "banana" -> 6 -> "banana"
"""
Problem 6: List Nodes
Write a function listify_first_n() that takes in a head of a linked list and a non-negative integer n as parameters.

The function returns a list of values of the first n nodes.

If n is greater than the length of the linked list, return a list of the values of all nodes in the linked list.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def listify_first_n(head, n):
    current = head
    output = []
    while current:
        output.append(current.value)
        current = current.next
    # Check if n is less than the length of output
    if n < len(output):
        # return the length up to n if it is
        return output[0:n]
    # If not return all
    return output    
# linked list: a -> b -> c
c = Node("c")
b = Node("b", c)
a = Node("a", b)
head = a
lst = listify_first_n(head,2)
print(lst)

# linked list: j -> k -> l 
l = Node("l")
k = Node("k", l)
j = Node("j", k)
head2 = j
lst2 = listify_first_n(head2,5)
print(lst2)
print()
"""
Problem 7: Insert Value
Write a function ll_insert() that takes in a head of a linked list, a value val, and an index i as parameters.

The function should insert a new Node with value val at index i of the linked list, then return the head of the linked list.

If i is greater than the length of the list, insert the new node at the end of the list.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def ll_insert(head, val, i):
    # Insert at the head of the list
    if i == 0:
        new_node = Node(val, head)
        return new_node
    current = head
    index = 0
    # Traverse the list to find the insertion point
    while current:
        if index == i - 1:
            new_node = Node(val, current.next)
            current.next = new_node
            break
        current = current.next
        index += 1
    else:
        current.next = Node(val)  # Insert at the end if index is out of range
    # Print the updated linked list
    current = head
    while current:
        if current.next:
            print(current.value, end=" -> ")
        else:
            print(current.value)
        current = current.next
    return head
    
head = Node(3, Node(8, Node(12, Node(9))))
ll_insert(head, 20, 2)
# result linked list: 3 -> 8 -> 20 -> 12 -> 9
print()
"""
Problem 8: Linked Listify
Write a function list_to_linked_list() that takes in a list lst as a parameter and converts it to a linked list. The function should return the head of the linked list.
"""
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
		
def list_to_linked_list(lst):
    if not lst:
        return None  # Return None for an empty list
    head = Node(lst[0])  # Create the head node
    current = head
    for value in lst:
        current.next = Node(value)  # Create the next node
        current = current.next
    # Print the linked list
    current = head
    return current.value
    
normal_list = ["Betty", "Veronica", "Archie", "Jughead"]
linked_list = list_to_linked_list(normal_list)
print(linked_list)
print()
"""
Problem 9: Doubly Linked List
One of the drawbacks of a linked list is that it's difficult to go backwards, because each Node only knows about the Node in front of it. (E.g., A -> B -> C)

A doubly linked list solves this problem! Instead of just having a next attribute, a doubly linked list also has a prev attribute that points to the Node before it. (E.g., A <-> B <-> C)

Given the Node class for a doubly linked list below, recreate the list ["Poliwag", "Poliwhirl", "Poliwrath"] as a doubly linked list.
"""
class Node:
	def __init__(self, value, next = None, prev = None):
		self.value = value
		self.next = next
		self.prev = prev
  
print(poliwhirl.prev.value, "<->", poliwhirl.value, "<->", poliwhirl.next.value)
