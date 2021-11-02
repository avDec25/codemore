# Given some intervals tell if a person can attend all the meetings
from typing import List

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort()
        le = -1
        for s, e in intervals:
            if le <= s:
                le = e
            else:
                return False

        return True

times = [[5, 10], [0, 30], [15, 20]]
Solution().canAttendMeetings(times)
