class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        mid=len(nums)//2
        sum=0
        for i in range(len(nums)):
            sum=sum+abs(nums[i]-nums[mid])
        return sum
