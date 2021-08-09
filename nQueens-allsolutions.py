from typing import List

# places queen column by column, 
# try each row for in the column, before moving onto the next column

class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    solution = list()
    ans = [["." for i in range(n)] for j in range(n)]
    
    def isSafe(r, c) -> bool:
      # check for any queen on the left side      
      # checking in left row
      for j in range(c):
        if ans[r][j] == "Q":
          return False
      
      # checking in upper left diagonal
      i, j = r-1, c-1
      while i >= 0 and j >= 0:
        if ans[i][j] == "Q":
          return False        
        i, j = i-1, j-1
        
      # checking in bottom left diagonal
      i, j = r+1, c-1
      while i < n and j >= 0:
        if ans[i][j] == "Q":
          return False
        i, j = i+1, j-1
        
      return True
    
    def solve(col) -> bool:
      if col >= n:
        solution.append(["".join(c) for c in ans])
      
      for row in range(n):
        if isSafe(row, col):
          ans[row][col] = "Q"
          solve(col+1)
          ans[row][col] = "."
    
    solve(0)
    return solution
    
n = 4
ans = Solution().solveNQueens(n)
print(ans)
