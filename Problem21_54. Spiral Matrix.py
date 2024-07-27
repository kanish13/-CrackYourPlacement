# 54. Spiral Matrix Link: https://leetcode.com/problems/spiral-matrix/description/

# Solution:

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rb=0
        re=len(matrix)-1
        cb=0
        ce=len(matrix[0])-1
        x=[]
        while (rb<=re and cb<=ce):
            if rb<=re:
                for i in range(cb,ce+1):
                    x.append(matrix[rb][i])
                rb=rb+1
            if cb<=ce:
                for i in range(rb,re+1):
                    x.append(matrix[i][ce])
                ce=ce-1
            if rb<=re:
                for i in range(ce,cb-1,-1):
                    x.append(matrix[re][i])
                re=re-1
            if cb<=ce:
                for i in range(re,rb-1,-1):
                    x.append(matrix[i][cb])
                cb=cb+1
        return x
        
        
