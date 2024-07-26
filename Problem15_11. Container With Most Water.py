# 11. Container With Most Water Link:https://leetcode.com/problems/container-with-most-water/description/

# Solution:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        x=0
        while l<r:
            if (r-l)*min(height[l],height[r])>x:
                x=(r-l)*min(height[l],height[r])
            if height[l]<height[r]:
                l=l+1
            else:
                r=r-1
        return x

