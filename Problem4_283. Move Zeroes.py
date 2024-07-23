# 283. Move Zeroes Link: https://leetcode.com/problems/move-zeroes/description/

# Solution:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        l=0
        for i in range(len(nums)):
            if nums[i]!=0:
                t=nums[l]
                nums[l]=nums[i]
                nums[i]=t
                l=l+1
        
