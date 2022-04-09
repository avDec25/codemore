from typing import List

class Solution:
  def peakIndexInMountainArray(self, a: List[int]) -> int:
    l, r = 0, len(a)-1
    while l <= r:
      mid = l + (r-l)//2
      if mid >= 0 and mid+1 < len(a) and a[mid-1] < a[mid] > a[mid+1]:
        print(f"a[l]   = a[{l}] = {a[l]}")
        print(f"a[mid] = a[{mid}] = {a[mid]}")
        print(f"a[r]   = a[{r}] = {a[r]}")
        return mid
      if mid-1 > 0 and a[mid-1] > a[mid]:
        r = mid
      else:
        l = mid+1
    return l

a = [-6, -2, 0, 1, 2, 3, 5, 4, 2, 1]
Solution().peakIndexInMountainArray(a)