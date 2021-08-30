
class Solution:
    def func(self, a):
        n = len(a)
        mp = {}
        for i in range(n):
            mp[a[i]] = mp.get(a[i], 0) + 1
        
        count = 0
        for i in range(n):
            if (a[i] != 1000-a[i]) and 1000 - a[i] in mp:
                count += 1

        return count

tomatoes = [500, 400, 300, 200, 600, 700]
Solution().func(tomatoes)
