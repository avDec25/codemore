from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        print(f"slow = {slow}")
        print(f"fast = {fast}")
        
        fast = 0
        while(slow != fast):
            fast = nums[fast]
            slow = nums[slow]
        return slow

nums = [1,3,4,2,2]
Solution().findDuplicate(nums)