# 974. Subarray Sums Divisible by K Link: https://leetcode.com/problems/subarray-sums-divisible-by-k/

# Solution:

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        s={0:1}
        res=0
        sum=0
        for i in range(len(nums)):
            sum=sum+nums[i]
            x=sum%k
            if x in s:
                res=res+s[x]
                s[x]=s[x]+1
            else:
                s[x]=1
        return res

