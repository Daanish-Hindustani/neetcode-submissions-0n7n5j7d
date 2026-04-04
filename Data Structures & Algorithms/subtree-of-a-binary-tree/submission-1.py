# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True 

        def isSame(node, subRoot):
            if not node and not subRoot:
                return True
            
            if node and subRoot and node.val == subRoot.val:
                return isSame(node.left, subRoot.left) and isSame(node.right, subRoot.right)

            return False

        
        def DFS(node, subRoot):
            if not node:
                return False
            
            if isSame(node, subRoot):
                return True
            
            return DFS(node.left, subRoot) or DFS(node.right, subRoot)
        return DFS(root, subRoot)
