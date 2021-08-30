# Minimum Number of Work Sessions to Finish the Tasks
from typing import List

class Solution:
    def minSessions(self, tasks: List[int], sessionTime: int) -> int:
        tasks.sort()
        n = len(tasks)
        count = 0
        total = 0
        for i in range(n):
            total += tasks[i]
            if total == sessionTime:
                total = 0
                count += 1
            elif total > sessionTime:
                total = tasks[i]
                count += 1
        print()
        if total > 0:
            count += 1
        return count


tasks = [7, 4, 3, 8, 10]
sessionTime = 12
Solution().minSessions(tasks, sessionTime)