class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        res = []
        max_val = nums[0]

        for r in range(len(nums)):
            max_val = max(nums[r], max_val)
            if r-l+1 == k:
                res.append(max_val)
                l += 1
        
        return res
            