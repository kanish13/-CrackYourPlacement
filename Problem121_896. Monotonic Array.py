class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        i=0
        d=0
        l=0
        r=1
        while r<len(nums):
            if nums[l] < nums[r]:
                if d==1:
                    return False
                i=1
            elif nums[l] > nums[r]:
                if i==1:
                    return False
                d=1
            l=l+1
            r=r+1
        return True
