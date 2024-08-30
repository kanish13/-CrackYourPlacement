class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x=[0]*len(nums)
        y=[]
        for i in nums:
            x[i-1]=i
        for i,j in enumerate(x):
            if j==0:
                y.append(i+1)
        return y
