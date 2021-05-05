from typing import List
import collections

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    sol = []
    mp = collections.defaultdict(set)
    for i,s in enumerate(strs):
      mp[''.join(sorted(s))].add(i)
      
    for key in mp.keys():
      indexes = mp.get(key)
      ans = []
      for i in indexes:
        ans.append(strs[i])
      sol.append(ans)
    return sol


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams(strs))


d = {}
for w in sorted(strs):  
  key = tuple(sorted(w))
  d[key] = d.get(key, []) + [w]

print(list(d.values()))