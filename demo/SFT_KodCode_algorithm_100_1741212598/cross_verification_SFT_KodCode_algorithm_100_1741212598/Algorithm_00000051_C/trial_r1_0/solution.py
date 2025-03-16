def enhanced_inorder_traversal(root: BinaryTreeNode | None) -> List[int]:
    """
    Performs an inorder traversal on a given BST and returns the values in sorted order.
    """
    if not root:
        return []
    
    stack, result = [], []
    current = root
    
    while stack or current:
        # Traverse to the farthest left node, pushing each encountered node onto the stack
        while current:
            stack.append(current)
            current = current.left_child
        
        # Pop the stack to get the farthest left node and add it to the result
        current = stack.pop()
        result.append(current.data)
        
        # Proceed to the right child
        current = current.right_child
    
    return result