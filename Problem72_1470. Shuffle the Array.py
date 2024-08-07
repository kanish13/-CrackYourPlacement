class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=[]
        i=0
        j=n
        while i<n and j<len(nums):
            x.append(nums[i])
            x.append(nums[j])
            i=i+1
            j=j+1
        return x

