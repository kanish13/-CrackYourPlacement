# 1423. Maximum Points You Can Obtain from Cards  Link: https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/description/

# Solution:

class Solution:
    def maxScore(self, nums: List[int], k: int) -> int:
        l=0
        r=len(nums)-k
        total=sum(nums[r:])
        res=total
        while r<len(nums):
            total=total+(nums[l]-nums[r])
            res=max(res,total)
            l=l+1
            r=r+1
        return res
