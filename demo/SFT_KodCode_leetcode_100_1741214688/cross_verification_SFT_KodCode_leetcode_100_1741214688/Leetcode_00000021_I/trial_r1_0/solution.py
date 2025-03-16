class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    stack = []
    current = root
    res = []
    
    while True:
        while current is not None:
            stack.append(current)
            current = current.left
        if not stack:
            break
        current = stack.pop()
        res.append(current.val)
        current = current.right
    
    if k <= len(res):
        return res[k-1]
    else:
        return None