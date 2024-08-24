class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        m=-1
        for i in range(len(arr)-1,-1,-1):
            curr=arr[i]
            arr[i]=m
            if curr>m:
                m=curr
        return arr
