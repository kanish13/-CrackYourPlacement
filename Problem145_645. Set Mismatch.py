class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        x=[0]*len(nums)
        y=[]
        for i in nums:
            if x[i-1]==0:
                x[i-1]=i
            else:
                y.append(i)
        for i in range(len(x)):
            if x[i]==0:
                y.append(i+1)
        return y
        

        
