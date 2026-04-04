class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        DIRECTIONS = [(1,0), (-1,0), (0,1), (0,-1)]
        q = deque([])
        count = 0
        max_time = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c,0))
                elif grid[r][c] == 1:
                    count += 1
                else:
                    continue
        
        while q:
            r,c,time = q.popleft()
            
            for row_val, col_val in DIRECTIONS:
                nbr_r = row_val + r
                nbr_c = col_val + c

                if 0<= nbr_r<ROWS and 0<=nbr_c<COLS and grid[nbr_r][nbr_c] == 1:
                    count -= 1
                    grid[nbr_r][nbr_c] = 2
                    q.append((nbr_r,nbr_c,time+1))
                    max_time = time + 1

        return -1 if count > 0 else max_time
