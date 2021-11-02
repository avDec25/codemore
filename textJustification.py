from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        curr, num_of_letters, res = [], 0, []
        for w in words:
            if len(w) + num_of_letters + len(curr) > maxWidth:
                # add spaces to words
                for space in range(maxWidth - num_of_letters):
                    curr[space % (len(curr)-1 or 1)] += ' '
                
                res.append(''.join(curr))
                num_of_letters = 0
                curr = []
        
            curr += [w]
            num_of_letters += len(w)
    
        return res + [' '.join(curr).ljust(maxWidth)]

words = ["This", "is", "an", "example", "of", "text", "justification.", "If", "I", "add", "more", "data", "into", "this", "then", "ok"]
maxWidth = 16
ans = Solution().fullJustify(words, maxWidth)
print(ans)
for line in ans:
    print(line)