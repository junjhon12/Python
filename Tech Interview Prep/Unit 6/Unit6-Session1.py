'Problem 1'
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next
  
def print_next(node):
    current = node
    while current:
        if current.next:
            print(current.value, end='->')
        else:
            print(current.value)
        current = current.next

head = Node(4, Node(3, Node(2)))
print_next(head)
print()

'Problem 2: Find Frequency'
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

def count_element(head, val):
    count = 0
    current = head
    while current:
        if current.value == val :
            count += 1
        current = current.next
    return count
head = Node(3, Node(1, Node(2, Node(1))))
print(count_element(head, 1))
print()

'Problem 3: Remove Tail'
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        
        
# Helper function to print the linked list
def print_list(node):
    current = node
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()

def remove_tail(head):
    if head is None:  # If the list is empty, return None
        return None
    if head.next is None:  # If there's only one node, removing it leaves the list empty
        return None 

    # Start from the head and find the second-to-last node
    current = head
    while current.next.next:  # Check the node after the next node
        current = current.next
    current.next = None  # Remove the last node by setting second-to-last node to None
    return head

head3 = Node(1, Node(2, Node(3, Node(4))))
print_list(remove_tail(head3))
print()
'Problem 4: Find the Middle'
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next

def find_middle_element(head):
    # If the list is empty, return None
    if head is None:
        return None

    # Initialize two pointers, slow and fast. Both start at the head of the list.
    slow = head
    fast = head

    # Iterate through the list. The fast pointer moves two steps at a time,
    # while the slow pointer moves one step at a time.
    while fast and fast.next:
        slow = slow.next  # Move slow pointer one step forward
        fast = fast.next.next  # Move fast pointer two steps forward

    # When the fast pointer reaches the end, the slow pointer will be at the middle element.
    return slow
    
head = Node(1, Node(2, Node(3, Node(4))))
print(find_middle_element(head).value)
print()
'Problem 5: Is Palindrome?'
class Node:
   def __init__(self, value, next=None):
       self.value = value
       self.next = next
def is_palindrome(head):
    # If the list is empty or has only one element, it's a palindrome
    if not head or not head.next:
        return True
    # Find the middle of the list using the fast and slow pointer technique
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Reverse the second half of the list
    prev = None
    while slow:
        # Store the next node
        next_node = slow.next
        # Reverse the current node's pointer
        slow.next = prev
        # Move the 'prev' pointer one step forward
        prev = slow
        # Move the 'slow' pointer one step forward
        slow = next_node
    # Compare the first half and the reversed second half
    left = head
    right = prev
    while right:  # We only need to compare until the end of the reversed half
        if left.value != right.value:
            return False
        left = left.next
        right = right.next
    return True

head = Node(1, Node(2, Node(1)))
print(is_palindrome(head))