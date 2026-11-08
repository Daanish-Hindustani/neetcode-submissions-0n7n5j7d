class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        sol = []


        def dfs(openN, closeN):
            if closeN == openN == n:
                res.append("".join(sol))
                return
            
            if openN < n:
                sol.append("(")
                dfs(openN + 1, closeN)
                sol.pop()
            
            if closeN < openN:
                sol.append(")")
                dfs(openN, closeN + 1)
                sol.pop()

            
        dfs(0,0)
        return res
            
            