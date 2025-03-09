class TreeNode:
    """Simple Binary Tree Node class."""
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def mirror_tree(node):
    """
    Converts a binary tree into its mirror tree.
    :param node: TreeNode, the root of the binary tree.
    :return: TreeNode, the root of the mirror tree.
    """
    if node is None:
        return None
    # Swap the left and right children
    node.left, node.right = node.right, node.left
    # Recursively apply to the left and right children
    mirror_tree(node.left)
    mirror_tree(node.right)
    return node