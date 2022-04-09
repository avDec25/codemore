from typing import List
import bisect

# class Solution:
#   def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
#     nr = len(matrix)
#     nc = len(matrix[0])

#     all_elements = []
#     for r in range(nr):
#       all_elements += matrix[r]

#     index = bisect.bisect_left(all_elements, target)
#     if index == len(all_elements):
#       return False

#     return all_elements[index] == target

class Solution:
  def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    nr = len(matrix)
    nc = len(matrix[0])

    l, r = 0, nr*nc-1
    while l <= r:
      mid = (l+r)//2
      middle_element = matrix[mid//nc][mid%nc]
      if middle_element == target:
        return True
      elif middle_element < target:
        l = mid + 1
      else:
        r = mid - 1
    return False



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 10
Solution().searchMatrix(matrix, target)