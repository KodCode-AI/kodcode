To find the `k`th smallest element in a given binary search tree (BST) without modifying the tree, we can perform an in-order traversal. In-order traversal of a BST processes nodes in ascending order. This can be accomplished using either recursion or an iterative approach with a stack. Here, we'll use an iterative approach.

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def kth_smallest(root, k):
    """
    Find the kth smallest element in a Binary Search Tree without modifying the tree.
    """
    stack = []
    current = root

    while current or stack:
        # Reach the leftmost node of the current subtree
        while current:
            stack.append(current)
            current = current.left
        
        # Current must be None at this point
        current = stack.pop()
        k -= 1
        
        # If k becomes zero, we've found the kth smallest element
        if k == 0:
            return current.value
        
        # Move to the right subtree
        current = current.right