from typing import List
import collections

class TimeMap:

  def __init__(self):
    self.a = collections.defaultdict(list)


  def set(self, key: str, value: str, timestamp: int) -> None:
    self.a[key].append([timestamp, value])


  def get(self, key: str, timestamp: int) -> str:
    kList = self.a[key]
    l = 0
    r = len(kList)

    # Can apply bSearch because strictly increasing timestamp.set operations were performed
    while l < r:
      mid = (l+r) // 2
      if timestamp >= kList[mid][0]:
        l = mid+1
      else:
        r = mid

    return "" if r == 0 else kList[r-1][1]



# Your TimeMap object will be instantiated and called as such:
obj = TimeMap()
func = ["set","get","get","set","get","get"]
args = [["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]
for i in range(len(func)):
  command = f'obj.{func[i]}(*{args[i]})'  
  exec(f'print("{command} = " + str({command}))')
