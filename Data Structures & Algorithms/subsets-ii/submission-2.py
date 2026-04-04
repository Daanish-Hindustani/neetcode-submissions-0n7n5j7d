class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        sol = []

        def DFS(i):
            if i == len(nums):
                res.append(sol[:])
                return 
            
            
            
            sol.append(nums[i])
            DFS(i+1)
            sol.pop()
            while i+1<len(nums) and nums[i+1] == nums[i]:
                i+=1
            
            DFS(i+1)
        
        DFS(0)

        return res