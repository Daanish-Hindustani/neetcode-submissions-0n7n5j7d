# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # dfs for root

        def check(root_node, subroot_node):
            if not root_node and not subroot_node:
                return True
            
            if not root_node or not subroot_node:
                return False
            
            if root_node.val != subroot_node.val:
                return False

            return True and check(root_node.left, subroot_node.left) and check(root_node.right, subroot_node.right)

        def dfs(root):
            if not root:
                return False
            
            if root.val == subRoot.val:
                val = check(root, subRoot)
                if val == True:
                    return True
            
            left = dfs(root.left)
            right = dfs(root.right)

            return left or right
        

        return dfs(root)
        
                

            

        # check function for root

