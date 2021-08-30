class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        slot = 1
        for node in preorder.split(','):
            if slot == 0:
                return False
            if node == '#':
                slot -= 1
            else:
                slot += 1
        return slot == 0
        
preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Solution().isValidSerialization(preorder)