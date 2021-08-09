# Subarray Sums Divisible by K
from typing import List

class Solution:
    def subarraysDivByK(self, a: List[int], k: int) -> int:
        res = 0
        sum_remainder = {0: 1}
        cumm_sum = 0
        # print(f"a = {a}, k = {k}")
        for x in a:
            # print("====================================================")
            # print(f"x = {x}; cumm_sum = {cumm_sum}; sum_remainder = {sum_remainder}")
            # print("----------------------------------------------------")

            # remainder says we need cumm_sum more to be Divisible by K
            # cumm_sum also says until this point what is the remainder we can get
            cumm_sum = (cumm_sum + x) % k
            # print(f"cumm_sum = {cumm_sum}")

            # is that cumm_sum present in sum_remainder
            res += sum_remainder.get(cumm_sum, 0)
            # print(f"res = {res}")

            sum_remainder[cumm_sum] = sum_remainder.get(cumm_sum, 0) + 1
            # print(f"sum_remainder = {sum_remainder}\n")
        return res

nums = [4, 5, 0, -2, -3, 1]
k = 5
Solution().subarraysDivByK(nums, k)
