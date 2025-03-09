class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_paths(root, target, path_sum, current_sum=0, path=[]):
    """
    Returns all root-to-leaf paths in the tree where the sum of the path equals the target.
    """
    if root is None:
        return []

    current_sum += root.val
    path.append(root.val)

    if root.left is None and root.right is None:
        if current_sum == target:
            return [path.copy()]
        else:
            path.pop()
            return []

    left_paths = find_paths(root.left, target, path_sum, current_sum, path)
    right_paths = find_paths(root.right, target, path_sum, current_sum, path)

    path.pop()
    return left_paths + right_paths