# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        R: Given a binary tree return its depth
        I: We can rec. all the way down and use max to calc which node(l or r) has larger val
        D: What happens if None? How to figure out which side is larger?
        E:
            1) Recursivly iterate through the nodes
            2) at each node before iterating future 1+max(rec(left), rec(right))
            3) If none: return 0
        """

        if not root:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))