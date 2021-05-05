def search(nums, target):
  n = len(nums)
  if n == 0:
    return -1
  
  low = 0
  high = n-1

  first = nums[0]

  while low <= high:
    mid = low + (high-low)//2
    mid_val = nums[mid]

    if target == mid_val:
      return mid

    is_mid_big = mid_val >= first
    is_target_big = target >= first

    if is_mid_big == is_target_big:
      if mid_val < target:
        low = mid+1
      else:
        high = mid-1
    else:
      if is_mid_big:
        low = mid+1
      else:
        high = mid-1
    
  return -1

print(search([5, 6, 7, 8, 9, 10, 1, 2, 3, 4], 3))