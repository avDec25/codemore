# Back Tracking solution
def combinations(a, k):
  dp = {0: 1}

  def dynamic(a, target):
    res = dp.get(target, -1)
    if res != -1:
      return res

    ans = 0
    for i in range(0, len(a)):
      if a[i] <= target:
        ans += dynamic(a, target-a[i])

    dp[target] = ans
    return ans

  return dynamic(a, k)


def backtrack(candidate, a, target):
  if target >= 0:
    if target == 0:
      global count
      count = count + 1
    else:
      for i in range(0, len(a)):
        candidate.append(a[i])
        backtrack(candidate, a, target-a[i])
        candidate.pop()


a = [1, 2, 4]
k = 32
print(combinations(a, k))
