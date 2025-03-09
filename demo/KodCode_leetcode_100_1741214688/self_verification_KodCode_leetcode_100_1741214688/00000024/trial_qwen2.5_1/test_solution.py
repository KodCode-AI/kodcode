from solution import *

from solution import kthSmallest, TreeNode

def create_bst_from_levels(elements):
    if not elements:
        return None
    root = TreeNode(elements[0])
    queue = [root]
    i = 1
    while i < len(elements):
        current = queue.pop(0)
        if elements[i] is not None:
            current.left = TreeNode(elements[i])
            queue.append(current.left)
        i += 1
        if i < len(elements) and elements[i] is not None:
            current.right = TreeNode(elements[i])
            queue.append(current.right)
        i += 1
    return root

# Construct the example tree
root = create_bst_from_levels([5, 3, 6, 2, 4, None, None])

def test_kthSmallest():
    assert kthSmallest(root, 3) == 3  # 3rd smallest element
    assert kthSmallest(root, 1) == 2  # 1st smallest element
    assert kthSmallest(root, 5) == 6  # 5th smallest element
    assert kthSmallest(root, 6) == 5  # 6th smallest element, but 5 is the largest
    assert kthSmallest(create_bst_from_levels([1, None, 2, None, None, None, 3]), 1) == 1  # Smallest element
    assert kthSmallest(create_bst_from_levels([3, 1, 4, None, 2]), 1) == 1  # Smallest element in unbalanced tree
    assert kthSmallest(create_bst_from_levels([3, 1, 4, None, 2]), 3) == 3  # 3rd smallest element in unbalanced tree
    assert kthSmallest(create_bst_from_levels([3, 1, 4, None, 2]), 4) == 4  # 4th smallest element, root itself

test_kthSmallest()