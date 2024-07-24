# 73. Set Matrix Zeroes Link: https://leetcode.com/problems/set-matrix-zeroes/description/

# Solution:

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=[]
        c=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    r.append(i)
                    c.append(j)
        for i in range(len(matrix)):
            if i in r:
                for j in range(len(matrix[i])):
                    matrix[i][j]=0
            else:
                for j in range(len(matrix[i])):
                    if j in c:
                        matrix[i][j]=0
        return matrix

        



        
