class Solution:
    def countVowelPermutation(self, n: int) -> int:
        if n == 1:
            return 5

        MOD =  10**9 + 7
        sumPrevious = 4
        previous = [1 for _ in range(5)]
        current  = [0 for _ in range(5)]

        for i in range(2, n+1):
            current[0] = previous[1]
            current[1] = (previous[0] + previous[2]) % MOD
            current[2] = sumPrevious
            current[3] = (previous[2] + previous[4]) % MOD
            current[4] = previous[0]
            sumPrevious = 0
            for j in range(5):
                previous[j] = current[j]
                if j != 2:
                    sumPrevious += previous[j]            
            sumPrevious %= MOD
        return (current[0] + current[1] + current[2] + current[3] + current[4]) % MOD


n = 5
Solution().countVowelPermutation(n)