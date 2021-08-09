from typing import List
import math

class Solution:
  def coinChange(self, coins: List[int], amount: int) -> int:
    INF = math.inf
    dp = [0] + [INF] * amount
    
    for i in range(1, amount+1):
      for coin in coins:
        if i-coin >= 0:
          dp[i] = min(dp[i], dp[i-coin] + 1)
    print(dp)
    
    if dp[-1] == INF:
      return -1
    else:
      return dp[-1]


coins = [1, 2, 5]
amount = 11
Solution().coinChange(coins, amount)