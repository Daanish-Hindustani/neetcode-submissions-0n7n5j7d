class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        sol = []

        def DFS(i, curr_sum):
            if curr_sum == target:
                s=res.append(sol[:])
                return
            
            if i >= len(candidates) or curr_sum > target:
                return

            sol.append(candidates[i])
            DFS(i+1, curr_sum + candidates[i])

            sol.pop()

            while i+1 < len(candidates) and candidates[i+1] == candidates[i]:
                i+=1
            
            DFS(i+1, curr_sum)

        DFS(0,0)
        return res

