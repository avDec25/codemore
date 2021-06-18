from typing import List
import heapq

class Solution:
  def minRefuelStops(self, target: int, fuel: int, stations: List[List[int]]) -> int:
    pq = []
    res = i = 0
    while fuel < target:
      while i < len(stations) and stations[i][0] <= fuel:
        heapq.heappush(pq, -stations[i][1])
        i += 1

      if not pq: return -1
      fuel += -heapq.heappop(pq)
      res += 1

    return res

target = 100
startFuel = 10
stations = [[10,60],[20,30],[30,30],[60,40]]
Solution().minRefuelStops(target, startFuel, stations)
