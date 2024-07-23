# 287. Find the Duplicate Number: Link: https://leetcode.com/problems/find-the-duplicate-number/description/

# Solution:

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow=0
        fast=0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        slow=0
        while True:
            slow=nums[slow]
            fast=nums[fast]
            if slow==fast:
                break
        return slow
     
