# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        temp = deque([root])

        while temp:

            for i in range(len(temp)):
                popped_value = temp.popleft()

                if not popped_value:
                    continue
                
                if popped_value.left:
                    temp.append(popped_value.left)
                
                if popped_value.right:
                    temp.append(popped_value.right)
                
                res.append(popped_value.val)
        
        res.sort()

        return res[k-1]



        