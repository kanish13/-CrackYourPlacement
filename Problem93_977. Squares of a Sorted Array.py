class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        x=[0]*len(nums)
        j=len(nums)-1
        while l<=r:
            if nums[l]**2>nums[r]**2:
                x[j]=nums[l]**2
                l=l+1
            else:
                x[j]=nums[r]**2
                r=r-1
            j=j-1
        return x
            
