class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROW = len(board)
        COL = len(board[0])
        directions = [(1,0),(-1,0),(0,1),(0,-1)]

        def DFS(r,c):
            for new_r, new_c in directions:
                nbr_r, nbr_c = r+new_r, c+new_c
                if 0<=nbr_r<ROW and 0<=nbr_c<COL and board[nbr_r][nbr_c] == "O":
                    board[nbr_r][nbr_c] = "E"
                    DFS(nbr_r,nbr_c)



        for r in range(ROW):
            for c in range(COL):
                if (r == 0 or r == ROW - 1) and board[r][c] == "O":
                    board[r][c] = "E"
                    DFS(r,c)
                elif (c == 0 or c == COL - 1) and board[r][c] == "O":
                    board[r][c] = "E"
                    DFS(r,c)
                else:
                    continue

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "E":
                    board[r][c] = "O"
        
        
        