class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        x={}
        for i in nums:
            x[i]=x.get(i,0)+1
            if x[i]>len(nums)//2:
                return i
        
