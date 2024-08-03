class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[1]
        right=[1]
        x=1
        y=1
        z=[]
        for i in range(len(nums)-1):
            x=x*nums[i]
            left.append(x)
        for i in range(len(nums)-1,0,-1):
            y=y*nums[i]
            right.append(y)
        right=right[::-1]
        for i in range(len(nums)):
            z.append(left[i]*right[i])
        return z
