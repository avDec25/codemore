#%%
# LCS: Longest Common Subsequence
class Solution():
    def lcs(self, x, y):
        m = len(x)
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max( T[i-1][j], T[i][j-1] )
        return T[m][n]
    
    # https://www.hackerrank.com/challenges/dynamic-programming-classics-the-longest-common-subsequence/problem
    def printLCS(self, x, y):
        m = len(x)
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max(T[i-1][j], T[i][j-1])
        i = m
        j = n
        ans = []
        while i > 0 and j > 0:
            if x[i-1] == y[j-1]:
                ans.insert(0, x[i-1])
                i -= 1
                j -= 1
            elif T[i-1][j] > T[i][j-1]:
                i -= 1
            else:
                j -= 1
        return ''.join(ans)
    
    # length of longest common substring
    def lcsubstr(self, x, y):
        m = len(x)
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        ans = -1000
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = 0
                ans = max(T[i][j], ans)
        return ans
    
    # Length of shortest common supersequence
    def scs(self, x, y):
        m = len(x)
        n = len(y)
        lcs_len = self.lcs(x, y)
        return m + n - lcs_len
    
    # Minimum Number of insertion and deletion
    # to convert string x to string y
    def minDeletionsToConvert(self, x, y):
        m = len(x)
        n = len(y)
        lcs_len = self.lcs(x, y)
        return abs(m - lcs_len) + abs(n - lcs_len)
    
    # Longest Palindromic Subsequence length
    def lps(self, x):
        y = x[::-1]
        return self.lcs(x, y)
    
    # Min. deletion to convert to palindromic subsequence
    def minDeletionsToPalindromic(self, x):
        y = x[::-1]
        len_lcs = self.lcs(x, y)
        return len(x) - len_lcs
    
    # Print shortest common supersequence
    def printSCS(self, x, y):
        m = len(x)
        n = len(y)
        T = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if x[i-1] == y[j-1]:
                    T[i][j] = 1 + T[i-1][j-1]
                else:
                    T[i][j] = max( T[i-1][j], T[i][j-1] )
        i, j = m, n
        ans = []
        while i > 0 and j > 0:
            if x[i-1] == y[j-1]:
                ans.insert(0, x[i-1])
                i -= 1
                j -= 1
            elif T[i-1][j] > T[i][j-1]:
                ans.insert(0, x[i-1])
                i -= 1
            else:
                ans.insert(0, y[j-1])
                j -= 1
        
        while i > 0:
            ans.insert(0, x[i-1])
            i -= 1
        while j > 0:
            ans.insert(0, y[j-1])
            j -= 1
        return ans
        
x = "abac"
y = "cab"
Solution().printSCS(x, y)