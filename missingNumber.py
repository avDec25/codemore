from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        superset = set()
        for i in range(1, n+1):
            superset.add(i)
        for e in nums:
            superset.discard(e)
        return [i for i in superset]

nums = [4,3,2,7,8,2,3,1]
Solution().missingNumber(nums)