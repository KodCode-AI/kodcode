class Solution:
    def diameter_of_binary_tree(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_diameter = 0
        
        def helper(node):
            nonlocal max_diameter
            if not node:
                return 0
            left_depth = helper(node.left)
            right_depth = helper(node.right)
            current_diameter = left_depth + right_depth
            if current_diameter > max_diameter:
                max_diameter = current_diameter
            return 1 + max(left_depth, right_depth)
        
        helper(root)
        return max_diameter