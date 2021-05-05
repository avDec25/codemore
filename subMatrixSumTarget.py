def numSubmatrixSumTarget(a, target) -> int:
  H = len(a)
  W = len(a[0])
  for i in range(H):
    for j in range(1, W):
      a[i][j] += a[i][j-1]
  
  ans = 0
  for L in range(W):
    for R in range(L, W):
      mp = {0: 1}
      sum = 0
      for row in range(H):
        sum += a[row][R] - (a[row][L-1] if L > 0 else 0)
        ans += mp.get(sum-target, 0)
        mp[sum] = 1 + mp.get(sum, 0)
  
  return ans
  

a = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
target = 0
print("ans = {}".format(numSubmatrixSumTarget(a, target)))
