class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            mid=(l+r)//2
            if (mid-1<0 or nums[mid-1]!=nums[mid]) and (mid+1>len(nums)-1 or nums[mid+1]!=nums[mid]):
                return nums[mid]
            size=mid-1 if nums[mid-1]==nums[mid] else mid
            if size%2:
                r=mid-1
            else:
                l=mid+1
