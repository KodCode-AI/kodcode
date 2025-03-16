class BinaryTreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left_child: BinaryTreeNode | None = None
        self.right_child: BinaryTreeNode | None = None

def enhanced_inorder_traversal(root: BinaryTreeNode | None) -> list[int]:
    result = []
    stack = []
    current = root
    
    while True:
        # Traverse to the leftmost node
        while current is not None:
            stack.append(current)
            current = current.left_child
        
        # If the stack is empty, break the loop
        if not stack:
            break
        
        # Pop the node from the stack
        current = stack.pop()
        result.append(current.data)
        
        # Move to the right child
        current = current.right_child
    
    return result