class BinaryTreeNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.left_child: BinaryTreeNode | None = None
        self.right_child: BinaryTreeNode | None = None

def enhanced_inorder_traversal(root: BinaryTreeNode | None) -> list[int]:
    if root is None:
        return []
    
    stack = []
    result = []
    current = root
    
    while True:
        # Traverse all the way to the left
        while current:
            stack.append(current)
            current = current.left_child
        
        if not stack:
            break
        
        current = stack.pop()
        result.append(current.data)
        current = current.right_child
    
    return result

# Example usage
if __name__ == "__main__":
    def make_tree() -> BinaryTreeNode | None:
        root = BinaryTreeNode(15)
        root.left_child = BinaryTreeNode(10)
        root.right_child = BinaryTreeNode(25)
        root.left_child.left_child = BinaryTreeNode(6)
        root.left_child.right_child = BinaryTreeNode(14)
        root.right_child.left_child = BinaryTreeNode(20)
        root.right_child.right_child = BinaryTreeNode(60)
        return root

    tree = make_tree()
    result = enhanced_inorder_traversal(tree)
    print(result)  # Expected output: [6, 10, 14, 15, 20, 25, 60]