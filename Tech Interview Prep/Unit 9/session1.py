"""Problem 1: Is Symmetric Tree"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_symmetric(root):
    # Helper function to check if two trees are mirrors
    def is_mirror(left, right):
        if not left and not right:
            return True  # Both subtrees are empty
        if not left or not right:
            return False  # One subtree is empty, the other is not
        return (left.val == right.val and
                is_mirror(left.left, right.right) and
                is_mirror(left.right, right.left))

    if not root:
        return True  # An empty tree is symmetric
    return is_mirror(root.left, root.right)  # Check the left and right subtrees

# Example usage
node1 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
print(is_symmetric(node1))  # Expected output: True
node1 = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
print(is_symmetric(node1))  # Expected output: False
print()
"""Problem 2: Root-to-Leaf Paths"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def binary_tree_paths(root):
    # Helper function for DFS
    def dfs(node, path, paths):
        if not node:
            return  # Reached a leaf node

        path.append(str(node.val))  # Add current node to path

        if not node.left and not node.right:
            paths.append("->".join(path))  # Leaf node, add path to result
        else:
            dfs(node.left, path, paths)  # Recurse on left child
            dfs(node.right, path, paths)  # Recurse on right child

        path.pop()  # Backtrack

    paths = []  # List to store all paths
    dfs(root, [], paths)  # Start DFS from the root
    return paths

# Example usage
root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3))
print(binary_tree_paths(root))  # Expected output: ["1->2->5", "1->3"]
root = TreeNode(1)
print(binary_tree_paths(root))  # Expected output: ["1"]
print()
"""Problem 3: Minimum Difference in BST"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_diff_in_bst(root):
    # Helper function for in-order traversal
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    nodes = inorder(root)  # Get sorted node values
    return min(nodes[i+1] - nodes[i] for i in range(len(nodes) - 1))

# Example usage
root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(6))
print(min_diff_in_bst(root))  # Expected output: 1
root = TreeNode(1, TreeNode(0), TreeNode(48, TreeNode(12), TreeNode(49)))
print(min_diff_in_bst(root))  # Expected output: 1

print()

"""Problem 4: Increasing Order Search Tree"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def increasing_bst(root):
    # Helper function for in-order traversal
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)

    nodes = inorder(root)  # Get sorted node values
    new_root = current = TreeNode()  # Dummy node to start
    for val in nodes:
        current.right = TreeNode(val)  # Create right child only
        current = current.right
    return new_root.right  # Return the actual new root

def print_increasing_bst(root):
    result = increasing_bst(root)
    values = []
    while result:
        values.append(result.val)
        result = result.right
    print(" ".join(map(str, values)))

# Example usage
root1 = TreeNode(5, TreeNode(1), TreeNode(7))
print_increasing_bst(root1)  # Expected output: 1 5 7

root2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1), None), TreeNode(4)), TreeNode(6, None, TreeNode(8, TreeNode(7), TreeNode(9))))
print_increasing_bst(root2)  # Expected output: 1 2 3 4 5 6 7 8 9
print()
"""Problem 5: Equal Tree Split"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def can_split(root):
    # Helper function to count nodes
    def count_nodes(node):
        if not node:
            return 0
        return 1 + count_nodes(node.left) + count_nodes(node.right)

    total_nodes = count_nodes(root)
    if total_nodes % 2 != 0:
        return False  # If total nodes are odd, can't split equally

    def dfs(node):
        if not node:
            return 0
        left_nodes = dfs(node.left)
        right_nodes = dfs(node.right)
        # Check if left or right subtree is half of the total nodes
        if left_nodes == total_nodes // 2 or right_nodes == total_nodes // 2:
            return total_nodes  # Found a valid split
        return left_nodes + right_nodes + 1

    return dfs(root) != total_nodes  # If found valid split, return True

# Example usage
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, None, TreeNode(7)))
print(can_split(root))  # Expected output: True
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
print(can_split(root))  # Expected output: False