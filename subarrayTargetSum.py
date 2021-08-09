def subArrSum(a, k):
  n = len(a)
  mp = {0: 1}
  ans = 0
  sum = 0
  for i in range(0, n):
    sum += a[i]
    ans += mp.get(sum-k, 0)
    mp[sum] = mp.get(sum, 0) + 1
  return ans

a = [3, 4, 7, 2, -3, 1, 4, 2]
k = 7
print(subArrSum(a,k))
