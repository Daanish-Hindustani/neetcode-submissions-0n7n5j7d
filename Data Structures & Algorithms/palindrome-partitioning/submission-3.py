class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []


        def dfs(i):
            if i == len(s):
                res.append(sol.copy())
                return
            

            for j in range(i, len(s)):
                if ispal(s, i, j):
                    sol.append(s[i:j+1])
                    dfs(j+1)
                    sol.pop()

        

        def ispal(vals, l, r):
            
            while l<r:
                if vals[l] != vals[r]:
                    return False
                
                l += 1
                r -= 1
            
            return True

        dfs(0)
        return res