class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        q = deque([])
        directions = [(1,0),(-1,0), (0,1), (0,-1)]
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    q.append((r,c,0))

        while q:
            r,c,distance = q.popleft()
            for r_dir, c_dir in directions:
                nbr_r, nbr_c = r+r_dir, c+c_dir
                if 0<=nbr_r<len(grid) and 0<=nbr_c<len(grid[0]) and grid[nbr_r][nbr_c] != -1 and grid[nbr_r][nbr_c]!=0 and grid[nbr_r][nbr_c] == INF:
                    grid[nbr_r][nbr_c] = distance+1
                    q.append((nbr_r, nbr_c, distance + 1))
        

        
            

            
