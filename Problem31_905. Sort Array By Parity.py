class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        while l<r:
            if nums[r]%2==0 and nums[l]%2!=0:
                t=nums[l]
                nums[l]=nums[r]
                nums[r]=t
                l=l+1
                r=r-1
            elif nums[l]%2==0:
                l=l+1
            elif nums[r]%2!=0:
                r=r-1
        return nums
            

