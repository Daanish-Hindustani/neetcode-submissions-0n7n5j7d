
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def dfs(i, curr_sum):
            if i >=len(nums) or curr_sum>target:
                return
            
            if curr_sum == target:
                res.append(sol.copy())
                return
            
            sol.append(nums[i])
            dfs(i, curr_sum+nums[i])

            sol.pop()
            dfs(i+1, curr_sum)

        dfs(0,0)
        return res
