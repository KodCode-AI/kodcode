class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_paths(root, target, current_sum=0, path=[], paths=[]):
    """
    Finds all root-to-leaf paths in a binary tree where the sum of the path equals the target sum.

    Args:
    root (TreeNode): The root node of the binary tree.
    target (int): The target sum of the paths.
    current_sum (int): The current running sum of the path.
    path (list): The current path of node values.
    paths (list): A list of all paths that meet the criteria.

    Returns:
    list: A list of all root-to-leaf paths where the sum equals the target sum.
    """
    current_sum += root.val
    path.append(root.val)

    if not root.left and not root.right:  # If leaf node
        if current_sum == target:
            paths.append(path.copy())
        return paths

    if root.left:
        find_paths(root.left, target, current_sum, path, paths)
    if root.right:
        find_paths(root.right, target, current_sum, path, paths)

    path.pop()  # Backtrack
    return paths