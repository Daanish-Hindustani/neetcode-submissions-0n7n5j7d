class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def DFS(i):
            if i == len(nums):
                res.append(sol[:])
                return
            
            sol.append(nums[i])
            DFS(i+1)
            sol.pop()
            DFS(i+1)

        DFS(0)

        return res