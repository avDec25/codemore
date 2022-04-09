from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, a: List[int]) -> int:
        curr_max = 0
        max_so_far = 0
        for i in range(len(a)):
            if a[i] != 0:
                curr_max += 1
            else:
                curr_max = 0
            max_so_far = max(max_so_far, curr_max)
        return max_so_far

nums = [1,1,0,1,1,1]
Solution().findMaxConsecutiveOnes(nums)