import collections

class TimeMap:
  
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = collections.defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
      self.dic[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
      a = self.dic[key]
      l = 0
      r = len(a)
      while l < r:
        mid = l + (r-l)/2
        if a[mid][0] <= timestamp:
          l = mid + 1
        elif a[mid][0] > timestamp:
          r = mid
          
      return "" if r == 0 else a[r-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

inputs = ["TimeMap", "set", "get", "get", "set", "get", "get"]
inputs = [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
