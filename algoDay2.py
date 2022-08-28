#%%]
import collections
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        ans = collections.deque()
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            if left > right:
                ans.appendleft(pow(left, 2))
                l += 1
            else:
                ans.appendleft(pow(right, 2))
                r -= 1
        return list(ans)

nums = [-4,-1,0,3,10]
Solution().sortedSquares(nums)

# %%
class Solution:
    def rotate(self, a: List[int], k: int) -> List[int]:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(a)
        a[0:k], a[k:] = a[k+1:n], a[0:k+1]
        return a

nums = [1,2,3,4,5,6,7]
k = 3
Solution().rotate(nums, k)
# %%
import collections
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[fast], nums[slow] = nums[slow], nums[fast]

            if nums[slow] != 0:
                slow += 1
        print(nums)

nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
# %%
# two sum 2
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left, right = 0, n-1

        while left < right:
            if nums[left] + nums[right] == target:
                return [left+1, right+1]
            elif nums[left] + nums[right] > target:
                right -= 1
            else:
                left += 1
        
        return [left+1, right+1]
        
nums = [2,7,11,15]
target = 9
Solution().twoSum(nums, target)
# %%

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')
        return ' '.join([w[::-1] for w in words])

s = "Let's take LeetCode contest"
Solution().reverseWords(s)
# %%
