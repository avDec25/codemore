from typing import List


class Solution:
  def numUniqueEmails(self, emails: List[str]) -> int:
    ans = set()
    for email in emails:
      address = ""
      for x in email:
        if x == '+' or x == '@':
          break
        elif x == '.':
          pass
        else:            
          address = address + x
      domain = email.find("@")
      ans.add(address + email[domain:])
    print(ans)
    return len(ans)


emails = ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]
Solution().numUniqueEmails(emails)
