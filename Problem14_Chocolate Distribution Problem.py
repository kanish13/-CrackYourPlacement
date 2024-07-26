# Chocolate Distribution Problem Link: https://www.geeksforgeeks.org/problems/chocolate-distribution-problem3825/1

# Solution:

class Solution:
    def findMinDiff(self, A,N,M):
        # code here
        A.sort()
        l=0
        r=0
        x=max(A)
        for i in range(len(A)):
            l=i
            if i+(M-1)<len(A):
                r=i+(M-1) 
            else:
                 break
            if (A[r]-A[l]<x):
                x=A[r]-A[l]
        return x
            
