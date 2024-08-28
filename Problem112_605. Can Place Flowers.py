class Solution:
    def canPlaceFlowers(self, nums: List[int], n: int) -> bool:
        for i in range(len(nums)):
            if nums[i]==0 and (i==0 or nums[i-1]==0) and (i==len(nums)-1 or nums[i+1]==0):
                nums[i]=1
                n=n-1
        return n<1
