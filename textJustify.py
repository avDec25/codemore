from typing import List

class Solution:
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    res, cur, num_of_letters = [], [], 0
    for w in words:
      if len(w) + num_of_letters + len(cur) > maxWidth:
        for i in range(maxWidth - num_of_letters):
          cur[i % (len(cur)-1 or 1)] += ' '
        res.append(''.join(cur))
        cur, num_of_letters = [], 0
      
      cur += [w]
      num_of_letters += len(w)
    
    return res + [' '.join(cur).ljust(maxWidth)]


words = ["This", "is", "an", "example", "of", "text", "justification.", "If", "I", "add", "more", "data", "into", "this", "then."]
maxWidth = 16
for line in Solution().fullJustify(words, maxWidth):
  print(line)

