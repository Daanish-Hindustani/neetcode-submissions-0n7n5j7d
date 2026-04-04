class Solution:
    def rob(self, nums: List[int]) -> int:
        def DP(nums):
            t1, t2 = 0, 0
            for val in nums:
                temp = t1
                t1 = max(t1, t2+val)
                t2 = temp
            
            return t1
            
        if len(nums) == 0 or nums is None:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        return max(DP(nums[:-1]), DP(nums[1:]))
        