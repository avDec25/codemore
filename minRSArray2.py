from typing import List


class Solution:
  def findMin(self, nums: List[int]) -> int:
    l, r = 0, len(nums)-1

    while l < r:
      mid = (r+l) // 2
      if nums[mid] > nums[r]:
        l = mid+1
      else:
        r = mid if nums[r]!=nums[mid] else r - 1

    return nums[l]


nums = [3, 3, 1, 3]
Solution().findMin(nums)

# Find Minimum in Rotated Sorted Array II
# here duplicates are also present
# for nums = [3, 3, 1, 3]