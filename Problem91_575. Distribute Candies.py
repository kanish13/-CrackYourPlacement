class Solution:
    def distributeCandies(self, nums: List[int]) -> int:
        s=set()
        c=0
        for j in nums:
            if j not in s and c<len(nums)//2:
                c=c+1
            s.add(j)
        return c
