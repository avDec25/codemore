def maxSumMatrixSum(a) -> int:  
  def kadane(matrix):
    n = len(matrix)
    curr_max = matrix[0]
    max_so_far = matrix[0]
    for i in range(1, n):
      curr_max = max(curr_max + matrix[i], matrix[i])
      max_so_far = max(curr_max, max_so_far)
    return max_so_far
  
  maxSum = 0
  H = len(a)
  W = len(a[0])
  L = 0
  R = 0
  print(a)
  while L < W:
    if L == R:
      runningColSum = [0] * H
    
    for k in range(0, H):
      runningColSum[k] += a[k][R]
    
    sum = kadane(runningColSum)
    maxSum = max(maxSum, sum)
    R = R + 1
    if R == W:
      R = 0
      L = L + 1
  return maxSum
 

a = [[6, -5, -7, 4, -4], [-9, 3, -6, 5, 2], [-10, 4, 7, -6, 3], [-8, 9, -3, 3, -7]]
print("ans = {}".format(maxSumMatrixSum(a)))
