from typing import List
import itertools

class NumArray:
    def __init__(self, nums: List[int]):
        self.acc = list(itertools.accumulate(nums))
        self.acc.insert(0, 0)


    def sumRange(self, left: int, right: int) -> int:
        return self.acc[right+1] - self.acc[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)