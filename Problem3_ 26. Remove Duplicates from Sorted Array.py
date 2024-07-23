# 26. Remove Duplicates from Sorted Array Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/

# Solution :

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=1
        for r in range(1,len(nums)):
            if nums[l-1]!=nums[r]:
                nums[l]=nums[r]
                l=l+1
        return l
