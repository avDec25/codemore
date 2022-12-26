# %%
from typing import List
from typing import Optional
from collections import Counter
# %%

# %%
# Integer to Roman


class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I',
        }
        ans = ""
        for k in roman:
            ans += (num // k) * roman[k]
            num %= k
        return ans


num = 3
Solution().intToRoman(num)

# %%

# %%
# Number of Good Pairs


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return sum((i * (i - 1)) // 2 for i in Counter(nums).values())


nums = [1, 2, 3, 1, 1, 3]
Solution().numIdenticalPairs(nums)
# %%
# Jewels and Stones


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        s = Counter(stones)
        ans = 0
        for j in jewels:
            ans += s.setdefault(j, 0)
        return ans


jewels = "aA"
stones = "aAAbbbb"
Solution().numJewelsInStones(jewels, stones)
# %%
# How Many Numbers Are Smaller Than the Current Number


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count = [0 for _ in range(101)]
        ans = []
        for e in nums:
            count[e] += 1
        for i in range(1, 101):
            count[i] += count[i-1]
        for i in nums:
            if i == 0:
                ans.append(0)
            else:
                ans.append(count[i-1])
        return ans


nums = [6, 5, 4, 8]
Solution().smallerNumbersThanCurrent(nums)


# %%



# %%
