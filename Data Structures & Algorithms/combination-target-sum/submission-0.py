class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []

        def visit(i, curr_sum):
            if curr_sum == target:
                res.append(sub[:])
                return
            if i >= len(nums) or curr_sum>target:
                return
            
            sub.append(nums[i])
            visit(i, curr_sum + nums[i])
            sub.pop()
            visit(i+1, curr_sum)
        
        visit(0,0)

        return res

