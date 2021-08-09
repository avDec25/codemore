import numpy as np

def findMaxForm(strs, m, n) -> int:
  dp = [[0] * (n+1) for _ in range(m+1)]
  print("m: {} and n: {}".format(m, n))
  for x in strs:
    zeros = x.count('0')
    ones = x.count('1')
    for i in range(m, zeros-1, -1):
      for j in range(n, ones-1, -1):
        dp[i][j] = max(dp[i][j], 1 + dp[i-zeros][j-ones])
        print("x: {}".format(x))
        print("zeros: {} and ones: {}".format(zeros, ones))
        print("i: {} and j: {}".format(i, j))
        print(np.matrix(dp))
        print("")
    
    
    
  return dp[m][n]


if __name__ == '__main__':
  strs = ["10", "0001", "111001", "1", "0"]
  m = 5
  n = 3
  print(findMaxForm(strs, m, n))
  
