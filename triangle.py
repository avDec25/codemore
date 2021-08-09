import sys

INF = 200
triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
def minPath(triangle):
  INF = sys.maxsize
  dp = [[INF for i in range(len(triangle))] for j in range(len(triangle))]
  def f(t, r, c):
    print("r: {}, c: {}".format(r, c))
    if r >= len(t):
      return INF
    elif r == len(t)-1:
      dp[r][c] = t[r][c]
    else:
      try1 = dp[r+1][c]   if dp[r+1][c]   < INF else f(t, r+1, c)
      try2 = dp[r+1][c+1] if dp[r+1][c+1] < INF else f(t, r+1, c+1)
      dp[r][c] = t[r][c] + min(try1,try2)
    return dp[r][c]
  
  return f(triangle, 0, 0)

ans = minPath(triangle)
print(ans)
print(dp)
