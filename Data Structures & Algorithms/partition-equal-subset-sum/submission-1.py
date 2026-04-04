class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        if sum(nums)%2 != 0:
            return False
        
        memo = {}
        
        def DP(i, curr_sum):
            if curr_sum == target:
                return True 
            if i >= len(nums):
                return False 
            if (i, curr_sum) in memo:
                return memo[(i, curr_sum)]
            
            memo[(i, curr_sum)] = DP(i+1, curr_sum + nums[i]) or DP(i+1, curr_sum)

            return memo[(i, curr_sum)]
        return DP(0,0)