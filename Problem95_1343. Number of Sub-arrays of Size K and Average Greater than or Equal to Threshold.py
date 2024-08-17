class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l=0
        r=k
        summ=0
        for i in range(l,k):
            summ=summ+arr[i]
        c= 1 if summ/k>=threshold else 0
        while r<len(arr):
            summ=summ-arr[l]
            l=l+1
            summ=summ+arr[r]
            r=r+1
            if summ/k>=threshold:
                c=c+1
        return c
