class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        x=[0]*len(nums)

        s=[]

        for i,n in enumerate(nums):

            while s and n>s[-1][0]:
                sn,si=s.pop()
                x[si]=(i-si)

            s.append([n,i])
        return x

