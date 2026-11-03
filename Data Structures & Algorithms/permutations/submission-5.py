class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = nums.copy()

        def dfs(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            for j in range(i, len(nums)):
                sol[i], sol[j] = sol[j], sol[i]
                dfs(i+1)
                sol[i], sol[j] = sol[j], sol[i]
                
        
        dfs(0)
        return res
