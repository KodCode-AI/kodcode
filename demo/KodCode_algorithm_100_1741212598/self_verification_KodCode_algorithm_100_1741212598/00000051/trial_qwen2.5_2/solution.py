def enhanced_inorder_traversal(root: BinaryTreeNode | None) -> list[int]:
    """
    Returns the values of the nodes in a BST in sorted order using an iterative inorder traversal.
    """
    if not root:
        return []
    
    stack, result = [], []
    current = root
    
    while True:
        # Traverse to the leftmost node
        while current:
            stack.append(current)
            current = current.left_child
        
        if not stack:
            break
        
        # Process the node
        node = stack.pop()
        result.append(node.data)
        
        # Move to the right subtree
        current = node.right_child
    
    return result