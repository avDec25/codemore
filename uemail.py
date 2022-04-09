from typing import List

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        ans = set()
        for email in emails:
            domain = email.find('@')
            first = email[:domain]
            first = first.replace('.', '')
            plusSym = first.find('+')
            if plusSym > -1:
                first = first[:plusSym]
            last = email[domain:]
            ans.add( first + last )
        return len(ans)

emails = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
Solution().numUniqueEmails(emails)
