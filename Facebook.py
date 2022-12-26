# %%
# Product of Array Except Self
import heapq
from typing import List
import webbrowser


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1]*n
        suffix_prod = [1]*n
        ans = [1]*n
        prefix_prod[0] = nums[0]
        suffix_prod[n-1] = nums[n-1]
        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i-1]*nums[i]
        for i in range(n-2, 0, -1):
            suffix_prod[i] = suffix_prod[i+1]*nums[i]

        for i in range(n):
            if i == 0:
                ans[i] = suffix_prod[i+1]
            elif i == n-1:
                ans[i] = prefix_prod[i-1]
            else:
                ans[i] = suffix_prod[i+1]*prefix_prod[i-1]

        return ans


nums = [-1, 1, 0, -3, 3]
Solution().productExceptSelf(nums)
# %%
# K Closest Points to Origin


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest_points = []
        for i in range(len(points)):
            x, y = points[i]
            distance = x**2 + y**2
            heapq.heappush(closest_points, (distance, i))
        ans = []
        for i in range(k):
            ans.append(points[heapq.heappop(closest_points)[1]])
        return ans


points = [[3, 3], [5, -1], [-2, 4]]
k = 2
Solution().kClosest(points, k)

# %%
# Minimum Remove to Make Valid Parentheses


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()
                else:
                    s[i] = ''
        while stack:
            s[stack.pop()] = ''
        return ''.join(s)


s = "lee(t(c)o)de)"
Solution().minRemoveToMakeValid(s)

# %%
# Integer to English Words


class Solution:
    def numberToWords(self, num: int) -> str:
        to19 = "One Two Three Four Five Six Seven Eight Nine Ten Eleven Twelve "\
            "Thriteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
        print(to19[1])
        tens = "Twenty Thrity Fourty Fifty Sixty Seventy Eighty Ninety".split()

        def words(n):
            if n < 20:
                return to19[n-1:n]
            if n < 100:
                return [tens[n//10-2]] + words(n % 10)
            if n < 1000:
                return [to19[n//100-1]] + ['Hundred'] + words(n % 100)
            for p, w in enumerate(['Thousand', 'Million', 'Billion'], 1):
                if n < 1000**(p+1):
                    return words(n//1000**p) + [w] + words(n % 1000**p)
        return ' '.join(words(num)) or "Zero"


num = 123456
Solution().numberToWords(num)


# %%
# Word Break
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False for i in range(n+1)]
        dp[0] = True
        for i in range(1, n+1):
            for word in wordDict:
                if dp[i-len(word)] and s[i-len(word):i] == word:
                    dp[i] = True
        print(dp)
        return dp[-1]
    
s = "catsandog"
wordDict = ["cats","dog","sand","and","cat"]
Solution().wordBreak(s, wordDict)


# %%
# Valid Palindrome II
class Solution:
    def validPalindrome(self, s: str) -> bool:
    
    
s = "aba"
Solution().validPalindrome(s)
