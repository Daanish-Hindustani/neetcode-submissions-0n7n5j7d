# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def dfs(root, prev, isLeft):
            if not root:
                return True
            
            if not prev:
                return True and dfs(root.left, root, True) and dfs(root.right, root, False)

            if isLeft and root.val < prev.val:
                return True and dfs(root.left, root, True) and dfs(root.right, root, False)

            elif not isLeft and root.val > prev.val:
                return True and dfs(root.left, root, True) and dfs(root.right, root, False)
            else:
                return False and dfs(root.left, root, True) and dfs(root.right, root, False)
            
        return dfs(root, None, False)
            
            
            
            