# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        q = deque([root])
        res = []


        while q:
            temp = []
            for _ in range(len(q)):
                q_node = q.popleft()
                if q_node is None:
                    continue
                
                temp.append(q_node.val)
                q.append(q_node.left)
                q.append(q_node.right)
            if temp:
                res.append(temp[-1])
        
        return res


