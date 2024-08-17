class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        summ=0
        l=0
        r=k
        for i in range(l,k):
            summ=summ+nums[i]
        summ=summ
        avg=summ/k

        while r<len(nums):
            summ=summ-nums[l]
            l=l+1

            summ=summ+nums[r]
            r=r+1
            

            if avg<summ/k:
                avg=summ/k
        return avg



