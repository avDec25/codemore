from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> 'None':
        def findUnassigned():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        return (i, j)
            return -1, -1

        def solve():
            r, c = findUnassigned()
            if (-1, -1) == (r, c):
                return True

            for k in map(str, range(1, 10)):
                if isSafe(r, c, k):
                    board[r][c] = k
                    if solve():
                        return True
                    board[r][c] = '.'
        
        def isSafe(r, c, k):
            rowsafe = all(k != board[i][c] for i in range(9))
            colsafe = all(k != board[r][i] for i in range(9))
            sqasafe = all(k != board[i][j] for i in getRange(r) for j in getRange(c))

            return rowsafe and colsafe and sqasafe
        
        def getRange(x):
            x = x - x%3
            return range(x, x+3)

        solve()
        
        
board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
Solution().solveSudoku(board)
for i in range(9):
    for j in range(9):
        print(board[i][j], end=" ")
    print("")
