from rich.console import Console
from rich.traceback import install
# from rich import print
install()
console = Console()

class Solution(object):
    def mincostTickets(self, days, costs):
        dp = [0 for i in range(days[-1] + 1)]
        for i in range(days[-1] + 1):
            if i not in days:
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 7)] + costs[1],
                            dp[max(0, i - 1)] + costs[0],
                            dp[max(0, i - 30)] + costs[2])
            #     print(f"""
            #     dp[{i}] = min(dp[{max(0, i - 7)}] + {costs[1]},
            #                   dp[{max(0, i - 1)}] + {costs[0]},
            #                   dp[{max(0, i - 30)}] + {costs[2]})
            #     """)

            #     print(f"""
            #     dp[{i}] = min(dp[max(0, {i - 7})] + {costs[1]},
            #                   dp[max(0, {i - 1})] + {costs[0]},
            #                   dp[max(0, {i - 30})] + {costs[2]})
            #     """)

            #     print(f"""
            #     dp[{i}] = min({dp[max(0, i - 7)]} + {costs[1]},
            #                   {dp[max(0, i - 1)]} + {costs[0]},
            #                   {dp[max(0, i - 30)]} + {costs[2]})
            #     """)
            # console.log(log_locals=True)
        return dp[-1]


days = [1, 4, 6, 7, 8, 20]
costs = [2, 7, 15]
Solution().mincostTickets(days, costs)
