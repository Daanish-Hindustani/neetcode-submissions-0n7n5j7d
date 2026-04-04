class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        max_res = 0
        res = 0
        vari = [(1,0),(-1,0), (0,1), (0,-1)]

        def visit(r,c):
            nonlocal res
            if grid[r][c] == 1:
                res+= 1
                grid[r][c] = 0
                for r_val, c_val in vari:
                    nr, nc = r+r_val, c+c_val
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                        visit(nr, nc)
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = 0
                    visit(r,c)
                    max_res = max(max_res, res)
        
        return max_res