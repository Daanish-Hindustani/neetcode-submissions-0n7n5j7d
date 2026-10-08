# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        curr_max = 0
        def rec(root):
            if not root:
                return 0
            
            nonlocal curr_max

            left = rec(root.left)
            right = rec(root.right)

            curr_max = max(curr_max, left+right)

            return 1 + max(left, right)
        
        rec(root)

        return curr_max

