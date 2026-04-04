class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_oranges = 0
        count = 0
        q = deque([])
        final_time = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    num_oranges += 1
                elif grid[r][c] == 2:
                    q.append((r,c,0))
                else:
                    continue
        directions = [(1,0), (-1,0), (0,1), (0, -1)]    
        while q:
            r,c,time = q.popleft()
            for dir_r, dir_c in directions:
                nr,nc = r+dir_r, c+dir_c
                if num_oranges == 0:
                    return final_time
                if 0<=nr<len(grid) and 0<=nc<len(grid[0]) and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr,nc,time+1))
                    final_time = time + 1
                    num_oranges -= 1
        
        if num_oranges == 0:
            return final_time
        else:
            return -1