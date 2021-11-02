from typing import List
import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [math.inf] * amount
        for coin in coins:
            for amt in range(amount+1):
                if amt >= coin:
                    dp[amt] = min(dp[amt], dp[amt-coin] + 1)
        return -1 if dp[-1] == math.inf else dp[-1]

coins = [1,2,5]
amount = 11
Solution().coinChange(coins, amount)