class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root: TreeNode, k: int) -> int:
    stack = []
    current = root
    count = 0

    while True:
        # Traverse to the leftmost node
        while current is not None:
            stack.append(current)
            current = current.left

        if not stack:
            break  # All nodes processed

        # Pop the node from stack
        current = stack.pop()
        count += 1

        if count == k:
            return current.val

        # Move to the right subtree
        current = current.right

    return None  # if k is larger than the number of nodes