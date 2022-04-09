from typing import List
import functools


class Solution:
    def oddEvenJumps(self, a: List[int]) -> int:
        ans = 0
        n = len(a)

        def findNextJump(I, jumpType) -> int:
            allowedIndices = []

            def comparatorOdd(x, y):
                return x < y if a[x] == a[y] else a[x] < a[y]

            def comparatorEven(x, y):
                return x < y if a[x] == a[y] else a[x] > a[y]

            if jumpType == 1:
                for j in range(I+1, n):
                    if a[I] <= a[j]:
                        allowedIndices.append(j)
                if len(allowedIndices) > 0:
                    allowedIndices = sorted(
                        allowedIndices, key=functools.cmp_to_key(comparatorOdd))

            if jumpType == 0:
                for j in range(I+1, n):
                    if a[I] >= a[j]:
                        allowedIndices.append(j)
                if len(allowedIndices) > 0:
                    allowedIndices = sorted(allowedIndices, key=functools.cmp_to_key(
                        comparatorEven))

            if len(allowedIndices) > 0:
                print(allowedIndices)
                return allowedIndices[0]
            else:
                return I

        for candidate in range(n-1):
            print(f"\ncandidate = {candidate}")
            i = candidate
            # odd jump
            jumpType = 1
            while i < n:
                nj = findNextJump(i, jumpType)
                if i == nj:
                    if i == n-1:
                        ans += 1
                    break
                else:
                    i = nj

                print(f"nj = {nj}, jumpType = {jumpType}")

                if i == n-1:
                    ans += 1
                    break
                else:
                    if jumpType == 1:
                        jumpType = 0
                    else:
                        jumpType = 1

        return ans+1


arr = [1, 2, 3, 2, 1, 4, 4, 5]
Solution().oddEvenJumps(arr)
