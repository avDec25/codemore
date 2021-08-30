from functools import lru_cache

class Solution:
    @lru_cache(None)
    def step(self, current, final):
        if current == final:
            return 1

        if current > final:
            return 0

        return self.step(current + 1, final) \
        + self.step(current + 2, final) \
        + self.step(current + 3, final)

print(Solution().step(0, 100))
