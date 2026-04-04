# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        R: Return True if the BT has the same struture
        I: We just need to recusivly go down both trees at the same time
        D: How to go down both trees at the same time
        E: 
            1) recusvly go down both trees

        """

        def dfs(p, q):
            if not p and not q:
                return True
            elif not p or not q:
                return False
            else:
                if p.val!=q.val:
                    return False
                
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            
        
        return dfs(p,q)
