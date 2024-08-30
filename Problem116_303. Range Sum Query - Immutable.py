class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=[]
        x=0
        for i in nums:
            x=x+i
            self.nums.append(x)

    def sumRange(self, left: int, right: int) -> int:
        r=self.nums[right]
        l=self.nums[left-1] if left>0 else 0
        return r-l


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
