class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        res = []
        sol = []

        def DFS(i, curr_sum):
            
            if curr_sum == target:
                res.append(sol[:])
                return
            
            if i >= len(nums) or curr_sum > target:
                return
            

            sol.append(nums[i])
            DFS(i, curr_sum + nums[i])
            sol.pop()
            DFS(i+1, curr_sum)
        
        DFS(0,0)
        return res