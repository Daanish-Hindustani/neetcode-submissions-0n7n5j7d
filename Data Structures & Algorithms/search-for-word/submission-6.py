class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(i,r,c):
            if i == len(word):
                return True


            if not 0<r<ROWS or not 0<c<COLS or board[r][c] == '#' or board[r][c] != word[i]:
                return False
            
            board[r][c] = '#'
            res = dfs(i+1, r+1, c) or dfs(i+1, r-1, c) or dfs(i+1, r, c+1) or dfs(i+1, r, c-1)

            board[r][c] = word[i]
            return res

        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(0, r, c):
                    return True
        
        return False
        
        