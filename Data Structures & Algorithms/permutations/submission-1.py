class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = nums.copy()

        def visit(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            for j in range(i, len(nums)):
                sol[i],sol[j] = sol[j], sol[i]
                visit(i+1)
                sol[i],sol[j] = sol[j], sol[i]
        
        visit(0)

        return res