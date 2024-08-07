class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        r=0
        for i in nums:
            c=0
            while i:
                c=c+1
                i=i//10
            if c%2==0:
                r=r+1
        return r
