class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       boxes = defaultdict(list)
       rows = defaultdict(list)
       cols = defaultdict(list)
      
       for i in range(9):
          for j in range(9):
             if board[i][j] == ".":
                continue
             if board[i][j] in rows[i]:
                return False
             else: 
                rows[i].append(board[i][j])
             if board[i][j] in cols[j]:
                return False
             else: 
                cols[j].append(board[i][j])
             
             if board[i][j] in boxes[(i//3, j//3)]:
                return False 
             else:
                boxes[(i//3, j//3)].append(board[i][j])
       return True
