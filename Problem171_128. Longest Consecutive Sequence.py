class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        c=0
        s=set(nums)
        for i in nums:
            if i-1 not in s:
                num=i+1
                l=1
                while num in s:
                    l=l+1
                    num=num+1
                c=max(c,l)

        return c
