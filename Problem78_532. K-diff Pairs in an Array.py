class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        c=0
        nums.sort()
        l=0
        r=1
        while l<len(nums)-1 and r<len(nums):
            if nums[r]-nums[l]==k:
                l=l+1
                r=r+1
                c=c+1
                while r<len(nums) and nums[r]==nums[r-1]:
                    r=r+1
            elif nums[r]-nums[l]<k:
                r=r+1
            else:
                l=l+1
                if r-l==0:
                    r=r+1
        return c

