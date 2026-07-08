class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        for i in range(n):
            row_set = set()
            col_set = set()
            square_set = set()

            for col in range(9):
                if board[i][col] == '.':
                    continue
                elif board[i][col] in row_set:
                    return False
                row_set.add(board[i][col])
            
            for row in range(9):
                if board[row][i] == '.':
                    continue
                elif board[row][i] in col_set:
                    return False
                col_set.add(board[row][i])
            
            for row in range(3):
                for col in range(3):
                    r = (i // 3) * 3 + row
                    c = (i % 3) * 3 + col
                    if board[r][c] == '.':
                        continue
                    elif board[r][c] in square_set:
                        return False
                    square_set.add(board[r][c])


        return True    
                 