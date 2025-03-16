class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

def enhanced_inorder_traversal(root: BinaryTreeNode | None) -> List[int]:
    """
    Performs an inorder traversal on a given BST and returns the values in sorted order.
    """
    if not root:
        return []
    
    stack, result = [], []
    current = root
    
    while stack or current:
        while current:
            stack.append(current)
            current = current.left_child
        
        current = stack.pop()
        result.append(current.data)
        current = current.right_child
    
    return result