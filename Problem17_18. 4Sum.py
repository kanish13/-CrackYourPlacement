# 18. 4Sum Link: https://leetcode.com/problems/4sum/description/

# Solution:

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        x=[]
        if len(nums)<4:
            return x
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l=j+1
                r=len(nums)-1
                while l<r:
                    summ=nums[i]+nums[j]+nums[l]+nums[r]
                    if summ==target:
                        x.append([nums[i],nums[j],nums[l],nums[r]])
                        l=l+1
                        while nums[l]==nums[l-1] and l<r: l=l+1
                        r=r-1
                        while nums[r]==nums[r+1] and l<r : r=r-1
                    elif summ>target:
                        r=r-1
                    else:
                        l=l+1 
        return x
