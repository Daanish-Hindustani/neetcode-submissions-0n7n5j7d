class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sub = []

        def visit(i):
            if i == len(nums):
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            visit(i+1)
            sub.pop()
            visit(i+1)

        visit(0)
        return res