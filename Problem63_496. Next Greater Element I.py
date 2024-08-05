class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x=[]
        d={}

        for i in nums2:
            while x and x[-1]<i:
                d[x.pop()]=i
            x.append(i)
        for i in range(len(nums1)):
            nums1[i]=d[nums1[i]] if nums1[i] in d else -1
        return nums1

