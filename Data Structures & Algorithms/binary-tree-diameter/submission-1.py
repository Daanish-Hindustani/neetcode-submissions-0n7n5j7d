# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        res = 0

        def DFS(node):
            if not node:
                return 0

            nonlocal res
        
            left = DFS(node.left)
            right = DFS(node.right)

            val = 1 + max(left, right)
            
            res = max(res, left+right)

            return val
        
        DFS(root)
        return res