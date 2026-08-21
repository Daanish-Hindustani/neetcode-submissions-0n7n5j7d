class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        ROW_SET = defaultdict(set)
        COL_SET = defaultdict(set)
        SQ_SET = defaultdict(set)

        ROWS = len(board)
        COLS = len(board[0])

        for r in range(ROWS):
            for c in range(COLS):
                val = board[r][c]
                if val == '.':
                    continue
                if val in COL_SET[c]:
                    return False
                COL_SET[c].add(val)

                if val in ROW_SET[r]:
                    return False
                ROW_SET[r].add(val)

                if val in SQ_SET[(r//3, c//3)]:
                    return False
                SQ_SET[(r//3, c//3)].add(val)
        
        return True