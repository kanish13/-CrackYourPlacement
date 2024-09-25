class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p=[1]*len(nums)
        pref=1
        for i in range(len(p)):
            p[i]=pref
            pref=pref*nums[i]
        post=1
        for j in range(len(p)-1,-1,-1):
            p[j]=p[j]*post
            post=post*nums[j]
        return p

