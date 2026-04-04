class Solution:
    def rob(self, nums: List[int]) -> int:
        
        memo = {}

        def DP(i):
            if i >= len(nums):
                return 0

            if i in memo:
                return memo[i]

            memo[i] = max(nums[i] + DP(i+2), DP(i+1))
            return memo[i]

        return DP(0)    
            