# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        
        res = []

        q = deque([(root, 0)])
        
        curr_depth = 0
        while q:
            node, depth = q.popleft()
            if not node:
                continue
            

            if depth == curr_depth:
                res.append(node.val)
                curr_depth += 1
            
            q.append((node.right, depth + 1))
            q.append((node.left, depth + 1))
        
        return res



        