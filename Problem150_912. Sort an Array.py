class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(nums):
            mid=len(nums)//2
            left=nums[:mid]
            right=nums[mid:]

            if len(left)>1:
               merge(left)
            if len(right)>1:
               merge(right)

            i=0
            j=0
            k=0
            while i<len(left) and j<len(right):
                if left[i]<right[j]:
                    nums[k]=left[i]
                    i=i+1
                else:
                    nums[k]=right[j]
                    j=j+1
                k=k+1
            while i<len(left):
                nums[k]=left[i]
                i=i+1
                k=k+1
            while j<len(right):
                nums[k]=right[j]
                j=j+1
                k=k+1
        merge(nums)
        return nums

