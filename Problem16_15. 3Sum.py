# 15. 3Sum Link: https://leetcode.com/problems/3sum/description/

# Solution:

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        x=[]
        for i in range(len(nums)-2):
            if i>0 and nums[i]==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                sum=nums[i]+nums[l]+nums[r]
                if sum==0:
                    x.append([nums[i],nums[l],nums[r]])
                    l=l+1
                    while nums[l]==nums[l-1] and l<r:
                        l=l+1
                    r=r-1
                elif sum>0:
                    r=r-1
                else:
                    l=l+1
        return x

