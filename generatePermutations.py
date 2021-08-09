from typing import List
import string

class Solution:
    def all_permutations(self, n: int) -> int:
        s = [ch for ch in string.ascii_lowercase[:n]]

        def permute(s, i):
            if i == n:
                print(s)
            else:
                for j in range(i, n):
                    s[i], s[j] = s[j], s[i]
                    permute(s, i + 1)
                    s[i], s[j] = s[j], s[i]

        permute(s,0)


n = 5
Solution().all_permutations(n)

# ...         permute(s,2)
# ... 
# >>> n = 5
# >>> Solution().all_permutations(n)
# ['a', 'b', 'c', 'd', 'e']
# ['a', 'b', 'c', 'e', 'd']
# ['a', 'b', 'd', 'c', 'e']
# ['a', 'b', 'd', 'e', 'c']
# ['a', 'b', 'e', 'd', 'c']
# ['a', 'b', 'e', 'c', 'd']