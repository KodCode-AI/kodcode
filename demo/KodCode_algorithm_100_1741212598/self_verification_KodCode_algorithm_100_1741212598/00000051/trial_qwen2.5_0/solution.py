from typing import List, Optional

class BinaryTreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left_child: Optional[BinaryTreeNode] = None
        self.right_child: Optional[BinaryTreeNode] = None

def enhanced_inorder_traversal(root: Optional[BinaryTreeNode]) -> List[int]:
    """
    Perform an inorder traversal of a BST iteratively and return the sorted list of node values.
    """
    if root is None:
        return []
    
    stack = []
    current = root
    result = []
    
    while stack or current:
        # Reach the left most Node of the current Node
        while current:
            stack.append(current)
            current = current.left_child
        
        # Current must be None at this point
        current = stack.pop()
        result.append(current.data)
        
        # We have visited the node and its left subtree. Now, it's right subtree's turn
        current = current.right_child
    
    return result