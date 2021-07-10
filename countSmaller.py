from typing import Counter, List

class Solution:
  def countSmaller(self, nums: List[int]) -> List[int]:
    smaller = [0] * len(nums)
    def func(enum):
      half = len(enum) // 2
      if half:
        left, right = func(enum[:half]), func(enum[half:])
        m, n = len(left), len(right)
        i = j = 0
        while i < m or j < n:
          if j == n or i < m and left[i][1] <= right[j][1]:
            enum[i+j] = left[i]
            smaller[left[i][0]] += j
            # print(f'smaller[{left[i][0]}] += {j}')
            i += 1
          else:
            enum[i+j] = right[j]
            j += 1
      return enum

    func(list(enumerate(nums))) # contains index,element
    return smaller

nums = [7, 2, 5, 4, 1, 6]
Solution().countSmaller(nums) 
