from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        fp = open("ouput.txt", "w")
        l, r, hl, hr, total = 0, len(height)-1, 0, 0, 0
        while l < r:
            fp.write(f"height[l:{l}] = {height[l]} < height[r:{r}] = {height[r]}\n")
            if height[l] < height[r]: # means right mei bigger wall is present 
                # so we can count the l wall and max height[l] difference
                fp.write(f"hl = max({hl}, {height[l]})\n")
                hl = max(hl, height[l])
                fp.write("total += hl - height[l]\n")
                fp.write(f"total += {hl} - {height[l]}\n")
                total += hl - height[l]
                l += 1
            else:
                # so we can count the r wall and max height[r] difference
                fp.write(f"hr = max({hr}, {height[r]})\n")
                hr = max(hr, height[r])
                fp.write("total += hr - height[r]\n")
                fp.write(f"total += {hr} - {height[r]}\n")
                total += hr - height[r]
                r -= 1
            fp.write("\n=======================================================\n")
        return total

height = [0,1,0,2,1,0,1,3,2,1,2,1]
Solution().trap(height)