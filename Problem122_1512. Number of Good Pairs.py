class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        c=0
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
            if d[i]>1:
                c=c+(d[i]-1)
        return c
