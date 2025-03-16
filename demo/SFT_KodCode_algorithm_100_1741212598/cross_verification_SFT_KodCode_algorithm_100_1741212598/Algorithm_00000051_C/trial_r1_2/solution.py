def enhanced_inorder_traversal(root: BinaryTreeNode | None) -> List[int]:
    """
    Performs an inorder traversal on a given BST and returns the values in sorted order.
    """
    if not root:
        return []
    
    stack, result = [], []
    current = root
    
    while stack or current:
        # Traverse to the leftmost node
        while current:
            stack.append(current)
            current = current.left_child
        
        # Visit the node
        current = stack.pop()
        result.append(current.data)
        # Move to the right subtree
        current = current.right_child
    
    return result