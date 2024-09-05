class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        x=[[1]]

        for i in range(rowIndex):
            t=[0]+x[-1]+[0]
            r=[]
            for j in range(len(t)-1):
                r.append(t[j]+t[j+1])
            x.append(r)
        return x[-1]
