class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l=0
        r=len(nums)-1
        c=0
        while l<r:
            if nums[l]+nums[r]<target:
                c=c+(r-l)
                l=l+1
            else:
                r=r-1
        return c
