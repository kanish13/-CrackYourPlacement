class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s=[-1]*(len(nums)+1)
        for i in nums:
            s[i]=i
        for i in range(len(s)):
            if s[i]==-1:
                return i
        
            


        
