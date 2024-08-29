class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l=0
        r=sum(nums)

        for i,j in enumerate(nums):
            r=r-j
            if l==r:
                return i
            l=l+j
        return -1
