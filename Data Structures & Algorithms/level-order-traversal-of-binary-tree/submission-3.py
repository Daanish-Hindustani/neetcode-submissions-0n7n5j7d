# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        temp = deque([root])

        while temp:
            row_res = []
            for i in range(len(temp)):
                temp_val = temp.popleft()
                if not temp_val:
                    return []
                row_res.append(temp_val.val)

                if temp_val.left:
                    temp.append(temp_val.left)
                if temp_val.right:
                    temp.append(temp_val.right)

            res.append(row_res)
        return res