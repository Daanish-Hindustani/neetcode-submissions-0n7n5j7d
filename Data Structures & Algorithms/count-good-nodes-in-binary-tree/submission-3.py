# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        cnt = 0

        def dfs(root, prev_max):
            if not root:
                return
            
            nonlocal cnt

            if not prev_max:
                cnt += 1
                dfs(root.left, root.val)
                dfs(root.right, root.val)

            elif root.val >= prev_max:
                cnt += 1

                dfs(root.left, root.val)
                dfs(root.right, root.val)
            
            else:
                dfs(root.left, prev_max)
                dfs(root.right, prev_max)

        dfs(root, None)

        return cnt
                
                
                
        