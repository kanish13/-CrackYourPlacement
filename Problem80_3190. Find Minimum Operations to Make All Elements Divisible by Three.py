class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        c=0
        for i in nums:
            if i%3!=0 and ((i+1)%3==0 or (i-1)%3==0):
                c=c+1
        return c
