class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        c=0
        for i in range(len(grid)):
            for j in range(len(grid[i])-1,-1,-1):
                if grid[i][j]<0:
                    c=c+1
                else:
                    break
        return c
