def bs(a, target, searchFirst):
  low, high, res = 0, len(a)-1, -1
  while low <= high:
    mid = low + (high-low) // 2
    if a[mid] > target:
      high = mid - 1
    elif a[mid] < target:
      low = mid + 1
    else:
      res = mid
      if searchFirst:
        high = mid - 1
      else:
        low = mid + 1

  return res
      


nums = [5, 7, 7, 8, 8, 10]
target = 8
print([bs(nums, target, True), bs(nums, target, False)])
