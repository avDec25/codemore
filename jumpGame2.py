from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return 0
        l, r = 0, nums[0]
        jumps = 1
        while r < n-1:
            jumps += 1
            farthest = max(i+nums[i] for i in range(l, r+1))
            l, r = r, farthest
        return jumps

nums = [2,3,1,1,4]
Solution().jump(nums)