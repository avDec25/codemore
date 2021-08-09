def minOperations(n):
  ans = 0
  for i in range(1, n, 2):
    ans = ans + n - i

  return ans

print(minOperations(6))