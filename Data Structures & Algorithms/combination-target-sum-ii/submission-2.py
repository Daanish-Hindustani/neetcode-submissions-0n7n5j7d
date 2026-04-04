class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        sub = []
        candidates.sort()
        def visit(i, curr_sum):
            if curr_sum == target:
                res.append(sub[:])
                return
            
            if i >= len(candidates) or curr_sum > target:
                return
            
            sub.append(candidates[i])

            visit(i+1, curr_sum + candidates[i])

            sub.pop()

            while i+1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            visit(i+1, curr_sum)

        visit(0, 0)

        return res