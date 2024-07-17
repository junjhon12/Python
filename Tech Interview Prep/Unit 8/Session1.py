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
    def __init__(self, val, left=None, right=None) :
        self.val = val
        self.left = left
        self.right = right
    
def check_tree(root):
    if TreeNode