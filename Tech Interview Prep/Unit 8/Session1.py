"""Problem 1: Build a Binary Tree I"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
nodeOne = TreeNode(10)
nodeTwo = TreeNode(4)
nodeThree = TreeNode(6)

nodeOne.left = nodeTwo      # Left child is 4
nodeOne.right = nodeThree   # Right child is 6
print()
"""Problem 2: 3-Node Sum I"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    return root.val == root.left.val + root.right.val

root1 = TreeNode(10, TreeNode(4), TreeNode(6))
print(check_tree(root1)) 

root2 = TreeNode(5, TreeNode(3), TreeNode(1))
print(check_tree(root2))  
print()
"""Problem 3: 3-Node Sum II"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def check_tree(root):
    if not root:
        return False
    # Check and set left node if left node exist, if not 0
    left_val = root.left.val if root.left else 0
    # Check and set right node if right node exist, if not 0
    right_val = root.right.val if root.right else 0
    return root.val == left_val + right_val
    
root1 = TreeNode(10, TreeNode(10))
print(check_tree(root1))
root2 = TreeNode(5, TreeNode(3), TreeNode(2))
print(check_tree(root2))
root3 = TreeNode(5, None, TreeNode(2))
print(check_tree(root3))
root4 = None
print(check_tree(root4))
print()
"""Problem 4: Find Leftmost Node I"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if root is None:
        return None
    # While there is a left node,loop it
    while root.left:
        # set the root value to the founded left node
        root = root.left
    # Return the value of the left node
    return root.val

root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(left_most(root1))
root2 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(left_most(root2))
root3 = None
print(left_most(root3))
print()
"""Problem 5: Find Leftmost Node II"""
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def left_most(root):
    if root is None:
        return None
    # Loop if there is a left node
    while root.left:
        # Set new value to root
        root = root.left
    #Return the value of the last left node
    return root.val

root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(left_most(root1))
root2 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(left_most(root2))
root3 = None
print(left_most(root3))
print()
"""Problem 6: In-order Traversal"""
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def inorder_traversal(root):
    output = []  # This will store the values in inorder
    stack = []  # This is used to keep track of nodes
    current = root  # Start with the root node

    # Continue while there are nodes to be processed
    while current is not None or stack:
        # Reach the leftmost node of the current node
        while current is not None:
            stack.append(current)  # Push the node to the stack
            current = current.left  # Move to the left child

        # Current is None here, process the top node from the stack
        current = stack.pop()  # Get the top node
        output.append(current.val)  # Add the node's value to the output

        # Now, visit the right subtree
        current = current.right

    return output

root1 = TreeNode(1, None, TreeNode(2, TreeNode(3)))
print(inorder_traversal(root1))
root2 = None
print(inorder_traversal(root2))
root3 = TreeNode(1)
print(inorder_traversal(root3))
print()
"""Problem 7: Binary Tree Size"""
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def size(root):
    output = []  # This will store the values in inorder
    stack = []  # This is used to keep track of nodes
    current = root  # Start with the root node
    count = -1 # Store's count of tree nodes

    # Continue while there are nodes to be processed
    while current is not None or stack:
        # Reach the leftmost node of the current node
        while current is not None:
            stack.append(current)  # Push the node to the stack
            current = current.left  # Move to the left child

        # Current is None here, process the top node from the stack
        current = stack.pop()  # Get the top node
        output.append(current.val)  # Add the node's value to the output

        # Now, visit the right subtree
        current = current.right

    count = len(output)
    return count

root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(size(root1))
root2 = None
print(size(root2))
print()
"""Problem 8: Binary Tree Find"""
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def find(root, value):
    if root is None:
        return False  # If the tree is empty, return False
    # Check if the current node's value matches the target value
    if root.val == value:
        return True
    # Recursively check the left and right subtrees
    left = find(root.left, value)
    right = find(root.right, value)
    return left or right

root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(3)), TreeNode(5))
print(find(root1, 5))
print(find(root1, 10))
print()
"""Problem 9: Binary Search Tree Find"""
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def find_bst(root, value):
    if root is None:
        return False  # If the tree is empty, return False
    # Check if the current node's value matches the target value
    if root.val == value:
        return True
    # Recursively check the left and right subtrees
    left = find(root.left, value)
    right = find(root.right, value)
    return left or right

root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(find_bst(root1, 5))
print(find_bst(root1, 10))
print()
"""Problem 10: BST Descending Leaves"""
class TreeNode():
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
   
def descending_leaves(root):
    if root is None:
        return []

    # Helper function to traverse the tree and collect leaves
    def collect_leaves(node):
        if node.left is None and node.right is None:
            return [node.val]  # Base case: leaf node
        left_leaves = collect_leaves(node.left) if node.left else []
        right_leaves = collect_leaves(node.right) if node.right else []
        return right_leaves + left_leaves  # Concatenate right and left leaves
    
    return collect_leaves(root)

root1 = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
print(descending_leaves(root1))
root2 = TreeNode(10)
print(descending_leaves(root2))