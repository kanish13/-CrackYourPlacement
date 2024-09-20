class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s=set()
        x=[]
        for i in nums1:
            s.add(i)

        for j in nums2:
            if j in s and j not in x:
                x.append(j)   
        return x
