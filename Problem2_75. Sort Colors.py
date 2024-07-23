# 75. Sort Colors : Link:https://leetcode.com/problems/sort-colors/description/

# Solution:

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l,r=0,len(nums)-1
        i=0
        while(r>=i):
            if nums[i]==0:
                t=nums[l]
                nums[l]=nums[i]
                nums[i]=t
                l=l+1
            elif nums[i]==2:
                t=nums[r]
                nums[r]=nums[i]
                nums[i]=t
                r=r-1
                i=i-1
            i=i+1
        
