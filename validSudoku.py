from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def isSafe(x, y):
            for i in range(x+1, 9):
                if board[x][y] == board[i][y]:
                    return False
            for j in range(y+1, 9):
                if board[x][y] == board[x][j]:
                    return False
            return True

        def isSafeSquare(x, y):
            mp = set()
            for i in range(x, x+3):
                for j in range(y, y+3):
                    if board[i][j] != ".":
                        if board[i][j] in mp: return False
                        else: mp.add(board[i][j])
            print(mp)
            return True

        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if not isSafe(i, j):
                        return False
                if i % 3 == 0 and j % 3 == 0:
                    if not isSafeSquare(i, j):
                        return False

        return True
        

board = [
[".",".",".",".","5",".",".","1","."],
[".","4",".","3",".",".",".",".","."],
[".",".",".",".",".","3",".",".","1"],
["8",".",".",".",".",".",".","2","."],
[".",".","2",".","7",".",".",".","."],
[".","1","5",".",".",".",".",".","."],
[".",".",".",".",".","2",".",".","."],
[".","2",".","9",".",".",".",".","."],
[".",".","4",".",".",".",".",".","."]]
Solution().isValidSudoku(board)