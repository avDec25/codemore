from typing import List


class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    ans = []
    # print(nums)
    mp = {}
    for i,x in enumerate(nums):
      remainder = (target - x)
      # print(mp)
      # print("x: {}, i: {}, r: {}".format(x, i, remainder))
      # print("===========================")
      if (remainder in mp):
        ans.append(mp[remainder])
        ans.append(i)
        return ans
      else:
        mp[x] = i
        
    return ans

nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print("******************************")
print(sol.twoSum(nums, target))