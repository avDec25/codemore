import sys

def minMerge(a, dp, v, i, j):
  if i == j:
    return 0
  if v[i][j]:
    return dp[i][j]

  v[i][j] = True
  ans = sys.maxsize
  rangeTotal = 0
  for k in range(i, j+1):
    rangeTotal += a[k]

  for r in range(i+1, j+1):
    ans = min(ans, rangeTotal + minMerge(a, dp, v, i, r-1) + minMerge(a, dp, v, r, j))
  
  return ans


def mergeStones(stones, n):
  dp = [[0]*(n) for _ in range(n)]
  v = [[False]*(n) for _ in range(n)]

  return minMerge(stones, dp, v, 0, n-1)


if __name__ == '__main__':
  arr = [3, 2, 4, 1]
  n = len(arr)
  print(mergeStones(arr, n))

