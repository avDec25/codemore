# %%
# Longest Common Subsequence
import functools
import timeit


class Solution:
    @functools.cache
    def lcs(self, x, y, m, n):
        if m == 0 or n == 0:
            return 0
        if x[m-1] == y[n-1]:
            return 1 + self.lcs(x, y, m-1, n-1)
        else:
            return max(self.lcs(x, y, m, n-1), self.lcs(x, y, m-1, n))


x = "ABCDGH"
y = "AEDFHR"
t0 = timeit.default_timer()
Solution().lcs(x, y, len(x), len(y))
t1 = timeit.default_timer()
print(t1-t0)
print(Solution().lcs.cache_info())

# %%
# Longest Common Subsequence: with TOP DOWN approach
class Solution:
    def lcs(self, x, y, m, n):
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    T[i][j] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])

        return T[m][n]


x = "ABCDGH"
y = "AEDFHR"
t0 = timeit.default_timer()
Solution().lcs(x, y, len(x), len(y))
t1 = timeit.default_timer()
print(t1-t0)

# %%
# Longest common substring
# or length of longest common subarray
class Solution:
    # finds length of the longest common substring present
    def longest_common_substring(self, x, y, m, n):
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    T[i][j] = 0
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = 0
                ans = max(ans, T[i][j])
        return ans
x = "ABCDGH"
y = "ABDFHR"
Solution().longest_common_substring(x, y, len(x), len(y))
# %%
# Print LCS: longest common subsequence
class Solution:
    def printLCS(self, x, y, m, n):
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    T[i][j] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])

        ans = []
        i = m
        j = n
        while i > 0 and j > 0:
            if x[i-1] == y[j-1]:
                ans.insert(0, x[i-1])
                i -= 1
                j -= 1
            elif T[i-1][j] > T[i][j-1]:
                i -= 1
            else:
                j -= 1

        return "".join(ans)


x = "ABCDGH"
y = "ABDFHR"
Solution().printLCS(x, y, len(x), len(y))

# %%

# %%
# Shortest Common SuperSequence
# Merge both such that both sequences
# are maintained even in the merged string
# find the length of Shortest common supersequence
class Solution:
    def lcs(self, x, y):
        m = len(x)
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
        return T[m][n]

    def supersequence(self, x, y):
        len_lcs = self.lcs(x, y)
        return len(x) + len(y) - len_lcs


x = "abac"
y = "cab"
Solution().supersequence(x, y)

# %%

# %%
# Minimum Number of insertion and deletion
# to convert string x to string y
# replace is not there in operations, hence not a question of Edit Distance

# because this contains choice and asking for optimal(i.e. either min or max)
# hence it a question for DP
# it contains 2 strings and provide an output integer means
# we can apply LCS in this

# the only thing that remains unaffected during convertion
# is the longest common subsequence
class Solution:
    def lcs(self, x, y):
        m = len(x)
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
        return T[m][n]

    def minOperations(self, x, y):
        len_lcs = self.lcs(x, y)
        return abs(len(x) - len_lcs) + abs(len(y) - len_lcs)


A = "heap"
B = "pea"
# A -> lcs -> B
Solution().minOperations(A, B)

# %%
# Longest Palindromic Subsequence
class Solution:
    def lcs(self, x, y):
        m = len(x)
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
        return T[m][n]
    
    # length of longest palindromic subsequence
    def lps(self, x):
        y = x[::-1]
        return self.lcs(x, y)


seq = "cbbd"
Solution().lps(seq)

# %%
# Minimum number of deletions in a string to make it a palindrome
# longest the palindromic subsequence, minimum will be the deletions
class Solution:
    def minDeletions(self, x, m):
        y = x[::-1]
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i][j-1], T[i-1][j])
        return m - T[m][n]


seq = "aba"
Solution().minDeletions(seq, len(seq))
# %%
# Print: Shortest Common SuperSequence
class Solution:
    def printSCS(self, x, y, m, n):
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0:
                    T[i][j] = 0

        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])

        ans = []
        i = m
        j = n
        while i > 0 and j > 0:
            if x[i-1] == y[j-1]:
                ans.insert(0, x[i-1])
                i -= 1
                j -= 1
            elif T[i][j-1] > T[i-1][j]:
                ans.insert(0, y[j-1])
                j -= 1
            else:
                ans.insert(0, x[i-1])
                i -= 1
        while i > 0:
            ans.insert(0, x[i-1])
            i -= 1
        while j > 0:
            ans.insert(0, y[j-1])
            j -= 1
        return "".join(ans)


x = "abac"
y = "cab"
Solution().printSCS(x, y, len(x), len(y))
# %%
# length of Longest repeating subsequence in a string
# x = y = same-string to get lcs within itself it indices 
# are different then it will be counted as a different subsequence
class Solution:
    def lrs(self, x):
        y = x[::-1]
        m = len(x)
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1] and i != j:
                    T[i][j] = T[i-1][j-1] + 1
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
        return T[m][n]

s = "AABEBCDD"
Solution().lrs(s)
# %%
# Sequence Pattern Matching
class Solution:
    def lcs(self, x, y):
        m = len(x)
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
        return T[m][n]
    
    def spm(self, x, y):
        len_lcs = self.lcs(x, y)
        if len(x) == len_lcs:
            return True
        elif len(y) == len_lcs:
            return True
        else:
            return False
    
x = "AXY"
y = "ADXCPY"
Solution().spm(x, y)
# %%
# Minimum number of insertions in a string to make it palindrome
# this question is same as minimum number of deletion required
# for elements to be deleted, instead of deleting them, if same element
# on the other side of the string is inserted, then also it will become palindrome
# Hence, number of minimum deletion required in a string to make it palindrome
# is equal to the minimum number of insertions required in that string to make it palindrome
class Solution:
    def lcs(self, x):
        y = x[::-1]
        m = len(x)
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]: T[i][j] = 1 + T[i-1][j-1]
                else: T[i][j] = max(T[i-1][j], T[i][j-1])
        return m - T[m][n]
    
x = "abac"
Solution().lcs(x)