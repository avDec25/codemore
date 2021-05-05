def util(matrix, i, j):
  W = len(matrix[0])
  H = len(matrix)
  
  if i < 0 or i >= H or i<0 or j >= W:
    return -1
  
  top = util(matrix, i-1, j) if matrix[i][j] < matrix[i-1][j] else -1
  bottom = util(matrix, i+1, j) if matrix[i][j] < matrix[i+1][j] else -1
  left = util(matrix, i, j-1) if matrix[i][j] < matrix[i][j-1] else -1
  right = util(matrix, i, j+1) if matrix[i][j] < matrix[i][j+1] else -1
  
  return max([top, left, bottom, right])
  

def longestIncreasingPath(matrix):
  util(matrix, 0, 0)


matrix = [[3, 4, 5], [3, 2, 6], [2, 2, 1]]
print(longestIncreasingPath(matrix))
