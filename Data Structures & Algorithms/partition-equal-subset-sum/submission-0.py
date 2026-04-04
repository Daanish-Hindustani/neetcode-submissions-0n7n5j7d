class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        if sum(nums)%2 != 0:
            return False
        
        def DP(i, curr_sum):
            if curr_sum == target:
                return True 
            if i >= len(nums):
                return False 
            
            return DP(i+1, curr_sum + nums[i]) or DP(i+1, curr_sum)
        
        return DP(0,0)