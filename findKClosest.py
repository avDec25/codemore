from typing import List
import heapq

class Solution:
  def findClosestElements(self, a: List[int], k: int, x: int) -> List[int]:
    heap = [(abs(x-v), i) for i,v in enumerate(a)]
    heapq.heapify(heap)
    ans = [a[heapq.heappop(heap)[1]] for _ in range(k)]
    ans.sort()
    return ans

arr = [1, 2, 3, 4, 5]
k = 4
x = 3
Solution().findClosestElements(arr, k, x)

# class Solution:
#     def findClosestElements(self, a: List[int], k: int, x: int) -> List[int]:
#         n = len(a)
#         heap = []
#         for i in range(n):
#             heapq.heappush(heap, (abs(x-a[i]), i))
        
#         ans = list()
#         for i in range(k):
#             ans.append(a[heapq.heappop(heap)[1]])

#         return sorted(ans)