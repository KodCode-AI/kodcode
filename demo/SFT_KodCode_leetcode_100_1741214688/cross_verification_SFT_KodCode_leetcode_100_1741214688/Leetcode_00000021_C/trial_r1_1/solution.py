class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: TreeNode, k: int) -> int:
    count = 0  # To keep track of the count in in-order traversal

    def in_order(node):
        nonlocal count  # Access the count from the outer function
        if not node:
            return None  # No node to process
        # Traverse left subtree
        left_res = in_order(node.left)
        if left_res is not None:
            return left_res  # Left subtree contains the k-th element
        # Process current node
        count += 1
        if count == k:
            return node.val  # Found the k-th element
        # Traverse right subtree
        right_res = in_order(node.right)
        if right_res is not None:
            return right_res  # Right subtree contains the k-th element
        return None

    return in_order(root)  # Start the in_order traversal from root