class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        res = []
        sol = []

        def visit(i):
            if i == len(nums):
                res.append(sol[::])
                return
            
            if i>=len(nums):
                return
            
            sol.append(nums[i])
            visit(i+1)
            sol.pop()
            while i+1 < len(nums) and nums[i]==nums[i+1]:
                i+=1
            visit(i+1)
        
        visit(0)

        return res
