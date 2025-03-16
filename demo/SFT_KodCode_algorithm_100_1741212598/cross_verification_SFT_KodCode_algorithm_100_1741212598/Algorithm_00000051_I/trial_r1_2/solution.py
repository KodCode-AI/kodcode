class BinaryTreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left_child: BinaryTreeNode | None = None
        self.right_child: BinaryTreeNode | None = None

def enhanced_inorder_traversal(root: BinaryTreeNode | None) -> list[int]:
    result = []
    if not root:
        return result
    
    stack = []
    current = root
    
    while True:
        # Traverse to the leftmost node
        while current:
            stack.append(current)
            current = current.left_child
        
        if not stack:
            break
        
        # Visit the node
        node = stack.pop()
        result.append(node.data)
        
        # Move to the right child
        current = node.right_child
    
    return result