# 560. Subarray Sum Equals K Link: https://leetcode.com/problems/subarray-sum-equals-k/description/

# Solution:

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s={
        0:1
        }
        t=0
        x=0
        for i in range(len(nums)):
            t=t+nums[i]
            if t-k in s :
                x=x+s[t-k]
            if t in s:
                s[t]=s[t]+1
            else:
                s[t]=1
        return x
       
