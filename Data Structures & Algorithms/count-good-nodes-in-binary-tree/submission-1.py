# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        res = 0
        def DFS(node, prev):
            if not node:
                return
            nonlocal res

            if node.val>=prev:
                res += 1
                print(node.val)
            
            prev = max(prev, node.val)
            DFS(node.left, prev)
            DFS(node.right, prev)
        
        DFS(root, root.val)

        return res 
            

            