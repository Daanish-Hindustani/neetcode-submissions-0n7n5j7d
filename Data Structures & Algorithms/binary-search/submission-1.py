class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bst(l, r, target):
            if l > r:  # Corrected base case
                return -1
            
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target:
                return bst(l, mid - 1, target)
            else:
                return bst(mid + 1, r, target)
        
        return bst(0, len(nums) - 1, target)