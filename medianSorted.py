from typing import List

class Solution:
  def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    n1 = len(nums1)    
    n2 = len(nums2)
    i1, i2 = 0, 0
    merged = []
    while i1 < n1 and i2 < n2:
      if nums1[i1] <= nums2[i2]:
        merged.append(nums1[i1])
        i1 += 1
      else:
        merged.append(nums2[i2])
        i2 += 1

    while i1 < n1: 
      merged.append(nums1[i1])
      i1 += 1
    while i2 < n2: 
      merged.append(nums2[i2])
      i2 += 1

    if len(merged) % 2 == 0:
      mid = (n1 + n2)//2
      return (merged[mid] + merged[mid+1])/2
    else:
      mid = (n1 + n2)//2
      return merged[mid]