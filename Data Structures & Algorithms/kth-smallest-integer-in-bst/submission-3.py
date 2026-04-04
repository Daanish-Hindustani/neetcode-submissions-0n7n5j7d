# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        heap = []

        def dfs(root):
            nonlocal heap
            if not root:
                return
            
            heapq.heappush(heap, -1*root.val)
            
            while len(heap) > k:
                heapq.heappop(heap)
            
            dfs(root.left)
            dfs(root.right)
        
        dfs(root)
        return heap[0]*-1