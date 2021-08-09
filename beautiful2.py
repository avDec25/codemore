def constructArray(n, k):
  N = n
  ans = [0] * n
  x = 1
  y = k+1
  i = 0
  while k >= 0 and x <= y:
    ans[i] = x
    x = x + 1
    i = i+1
    if k < 0:
      break
    if k >=0 and x <= y:
      ans[i] = y
      y = y - 1
      i = i+1

  for i in range(k+2, n+1):
    ans[i] = i
  
  return ans

n = 5
k = 4
print(constructArray(n, k))