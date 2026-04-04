# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return False
            
            return valid_sub_tree(root, subRoot) or dfs(root.left) or dfs(root.right)


        def valid_sub_tree(root, subRoot):
            if root and not subRoot:
                return False
            
            if not root and subRoot:
                return False
            
            if not root and not subRoot:
                return True
            
            if root.val != subRoot.val:
                return False
            
            return True and valid_sub_tree(root.left, subRoot.left) and valid_sub_tree(root.right, subRoot.right)
            
        return dfs(root)
            