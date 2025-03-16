class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameter(root):
    if root is None:
        return 0
    max_diameter = [0]  # Using a list to allow modification in nested function

    def helper(node):
        if node is None:
            return 0
        left = helper(node.left)
        right = helper(node.right)
        # Calculate the diameter through this node
        current_diameter = left + right + 2
        # Update the maximum diameter found
        if current_diameter > max_diameter[0]:
            max_diameter[0] = current_diameter
        # Return the height of the current node
        return max(left, right) + 1

    helper(root)
    return max_diameter[0] if max_diameter[0] != 0 else 0