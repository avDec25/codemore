from typing import List
import string

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        letters = string.ascii_letters
        shift_by = 0
        ans = []
        for i in range(len(shifts)-1, -1, -1):
            shift_by += shifts[i]            
            ans.append(letters[(letters.find(s[i]) + shift_by)%26])
        return ''.join(ans[::-1])

s = "abc"
Solution().shiftingLetters(s, [3, 5, 9])
