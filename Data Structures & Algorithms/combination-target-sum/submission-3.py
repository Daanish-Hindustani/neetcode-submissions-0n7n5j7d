class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []
        def dfs(i, curr_sum):
            if curr_sum == target:
                res.append(sol[:])
                return
            
            for j in range(i, len(nums)):
                if nums[j] + curr_sum > target:
                    continue
                
                sol.append(nums[j])
                dfs(j, curr_sum+nums[j])

                sol.pop()
        
        dfs(0, 0)
    
        return res


            
            