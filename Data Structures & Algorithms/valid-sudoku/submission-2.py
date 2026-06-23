class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
         for every cell:
            does cell exist in square(3x3)
            does cell exist in row
            does cell exist in col
         
            if success:
               append to square hash
               append to row hash
               append to col has
        """

        ROWS = len(board)
        COLS = len(board[0])

        col_hash = defaultdict(list)
        row_hash = defaultdict(list)
        square_hash = defaultdict(list)

        for r in range(ROWS):
            for c in range(COLS):
                cell = board[r][c]
                if cell == ".":
                    continue
                
                if cell in col_hash[c]:
                    return False
               
                if cell in row_hash[r]:
                    return False
               
                if cell in square_hash[(r//3, c//3)]:
                    return False
               
                col_hash[c].append(cell)
                row_hash[r].append(cell)
                square_hash[(r//3, c//3)].append(cell)
         

        return True
