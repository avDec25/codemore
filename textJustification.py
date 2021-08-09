from typing import List
from math import floor

class Solution:
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    ans = []
    lines = dict()
    count = dict()
    w = 0
    i = 0
    for word in words:
      n = len(word)
      w += n
      if w > maxWidth:
        w = 0
        i += 1
      lines[i] = lines.get(i, []) + [word]
      count[i] = count.get(i, 0) + n
      w += 1
    
    print(count)
    for i in range(len(lines)):
      line = lines[i]
      minSpaces = len(line) - 1
      print("for line = {}, len = {}, minSpace = {}".format(line, len(line), minSpaces))
      if minSpaces + count.get(i) < maxWidth:
        if minSpaces > 1:
          avgSpaces = (maxWidth - count[i]) / minSpaces
          fractional = avgSpaces - floor(avgSpaces)
          if fractional > 0:
            avgLeftSpaces = floor((maxWidth - count[i] - floor(avgSpaces)) // (minSpaces-1))
            avgRightSpaces = floor(avgSpaces)
          else:
            avgLeftSpaces = floor(avgSpaces)
            avgRightSpaces = floor(avgSpaces)
          print("left = {}, right = {}\n".format(avgLeftSpaces, avgRightSpaces))      
      
      preparedLine = ""
      if len(line) == 1:
        preparedLine = line[0] + " " * (maxWidth - len(line[0]))
      else:
        for x in range(len(line)):
          preparedLine += line[x]
          if x == len(line)-2:
            preparedLine += " " * avgRightSpaces
          elif x == len(line)-1:
              pass
          else:
            preparedLine += " " * avgLeftSpaces
      ans.append(preparedLine)
      
    return ans


words = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth = 16
ans = Solution().fullJustify(words, maxWidth)
for x in ans:
  print(x)
