"""Problem 1: Is Symmetric Tree"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    # If the tree is empty, it is symmetric
    if root is None:
        return True

    # Helper function to check if two trees are mirror images of each other
    def is_mirror(left, right):
        # If both subtrees are empty, they are mirrors
        if not left and not right:
            return True
        # If one subtree is empty and the other is not, they are not mirrors
        if not left or not right:
            return False
        # Check if the current nodes have the same value and 
        # recursively check if the left subtree is a mirror of the right subtree
        # and the right subtree is a mirror of the left subtree
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    # Start the recursion with the left and right children of the root
    return is_mirror(root.left, root.right)
        
node1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(node1))
node1 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(is_symmetric(node1))
print()
"""Problem 2: Root-to-Leaf Paths"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def binary_tree_paths(root):
    # Helper function to perform DFS and build paths
    def dfs(node, path, paths):
        if not node:
            return  # If the node is None, return
        
        # Add the current node's value to the path
        path.append(str(node.val))
        
        # If it's a leaf node (no left and right children), add the path to the list of paths
        if not node.left and not node.right:
            paths.append("->".join(path))
        else:
            # Continue the DFS on the left and right children
            dfs(node.left, path, paths)
            dfs(node.right, path, paths)
        
        # Backtrack: remove the current node's value from the path
        path.pop()

    paths = []  # List to store all root-to-leaf paths
    dfs(root, [], paths)  # Start DFS from the root
    return paths

root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(binary_tree_paths(root))
root = TreeNode(1)
print(binary_tree_paths(root))