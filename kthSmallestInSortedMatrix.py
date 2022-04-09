from typing import List
import heapq

class Solution:
  def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    nr = len(matrix)
    nc = len(matrix[0])
    
    heap = []
    for r in range(nr):
      for c in range(nc):
        heapq.heappush(heap, matrix[r][c])

    for _ in range(k):
      nthSmallest = heapq.heappop(heap)
      
    return nthSmallest
      
  
matrix = [[1,5,9],[10,11,13],[12,13,15]]
k = 8
Solution().kthSmallest(matrix, k)