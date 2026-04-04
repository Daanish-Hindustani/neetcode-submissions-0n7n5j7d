class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if nums == []:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        def dp(num_list):
            t1, t2 = 0, 0
            for val in num_list:
                temp = t1
                t1 = max(t1, t2 + val)
                t2 = temp
            return t1
        
        return max(dp(nums[1:]), dp(nums[:-1]))