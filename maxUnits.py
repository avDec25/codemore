from typing import List
class Solution:
  def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
    boxTypes.sort(key= lambda x: -x[1])
    print(boxTypes)
    ans = 0

    for box, units in boxTypes:
      if truckSize > box:
        truckSize -= box
        ans += box * units
      else:
        ans += truckSize * units
        return ans
    
    return ans


boxTypes = [[5,10],[2,5],[4,7],[3,9]]
truckSize = 10
Solution().maximumUnits(boxTypes, truckSize)

boxTypes.sort(key= lambda x: -x[1])
print(boxTypes)