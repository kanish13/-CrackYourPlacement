# 34. Find First and Last Position of Element in Sorted Array Link: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

# Solution:

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l=0
        r=len(nums)-1
        x=[]
        while l<=r:
            if nums[l]==target and nums[r]==target:
                x.append(l)
                x.append(r)
                return x
            elif nums[l]==target:
                r=r-1
            elif nums[r]==target:
                l=l+1
            else:
                l=l+1
                r=r-1
        return [-1,-1]
