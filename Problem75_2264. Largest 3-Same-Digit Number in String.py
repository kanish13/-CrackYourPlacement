class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max=""
        nums=[int(x) for x in num]
        for i in range(len(nums)-2):
            if nums[i]==nums[i+1] and nums[i+1]==nums[i+2] and (max=="" or nums[i]>int(max) ):
                max=str(nums[i])
        return max*3

