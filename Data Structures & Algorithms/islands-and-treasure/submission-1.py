class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        INF = 2147483647
        DIRECTIONS = [(1,0),(-1,0),(0,1),(0,-1)]

        q = deque([])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        
        while q:
            r,c = q.popleft()
            for nr, nc in DIRECTIONS:
                new_r,new_c = nr+r, nc+c
                if 0<=new_r<ROWS and 0<=new_c<COLS and grid[new_r][new_c] != -1 and grid[new_r][new_c] == INF:
                    grid[new_r][new_c] =grid[r][c] + 1
                    q.append((new_r, new_c))
