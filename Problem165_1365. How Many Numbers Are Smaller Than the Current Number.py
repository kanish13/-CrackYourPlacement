class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        x=sorted(nums)
        d={}
        y=[0]*len(nums)
        for i in range(len(x)):
            if x[i] not in d:
               d[x[i]]=i
        for i in range(len(nums)):
            y[i]=d[nums[i]]
        return y
        
        


