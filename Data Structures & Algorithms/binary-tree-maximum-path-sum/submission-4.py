# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        res = root.val

        def DFS(node):
            if not node:
                return 0
            
            nonlocal res

            left = DFS(node.left)
            right = DFS(node.right)
            left = max(left, 0)
            right = max(right, 0)

            res = max(res, node.val+left+right)
            print(left, right)
            return node.val + max(left, right)
        
        DFS(root)

        return res