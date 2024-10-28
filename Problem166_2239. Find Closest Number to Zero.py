class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        minn=float("inf")
        for i in nums:
            if abs(i)<abs(minn):
                minn=i
        if minn<0 and abs(minn) in nums:
            return abs(minn)
        return minn
