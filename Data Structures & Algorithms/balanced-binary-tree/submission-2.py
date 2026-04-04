# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def DFS(node):
            if not node:
                return [True, 0]
            
            left = DFS(node.left)
            right = DFS(node.right)

            balanced = left[0] and right[0] and abs(left[1] - right[1]) < 2

            return [balanced, 1 + max(right[1], left[1])]
        
        return DFS(root)[0]

    