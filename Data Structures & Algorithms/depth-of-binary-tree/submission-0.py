# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def recurse(cur_depth, root):
            if root is None:
                return cur_depth
                
            left = root.left
            right = root.right
            final_depth = max(recurse(cur_depth + 1, left), recurse(cur_depth + 1, right))
            return final_depth

        return recurse(0, root)
