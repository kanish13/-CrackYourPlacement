# 442. Find All Duplicates in an Array: Link: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

# Solution:

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        s=set()
        x=[]
        for i in range(len(nums)):
            if nums[i] not in s:
                s.add(nums[i])
            else:
                x.append(nums[i])
        return x
