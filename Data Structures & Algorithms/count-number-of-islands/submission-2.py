class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        vari = [(1, 0), (-1, 0), (0,1), (0,-1)]
        count = 0 
        ROW, COL = len(grid), len(grid[0])


        def DFS(r,c):
            for dir_r, dir_c in vari:
                grid[r][c] = "0"
                nbr_r, nbr_c = r+dir_r, c+dir_c
                if 0<=nbr_r<ROW and 0<=nbr_c<COL and grid[nbr_r][nbr_c] == "1":
                    DFS(nbr_r,nbr_c)
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == "1":
                    DFS(r,c)
                    count+=1
        
        return count
            