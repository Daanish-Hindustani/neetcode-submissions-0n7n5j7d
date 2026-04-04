class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        vari = [(1, 0), (-1, 0), (0,1), (0,-1)]
        count = 0 
        def vist(r,c):
            if grid[r][c] == "1":
                
                grid[r][c] = "0"
                for r_val,c_val in vari:
                    nr = r + r_val
                    nc = c + c_val
                    if 0<=nr<len(grid) and 0<=nc<len(grid[0]):
                        vist(nr, nc)


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    vist(r,c)
                    count += 1
        
        return count