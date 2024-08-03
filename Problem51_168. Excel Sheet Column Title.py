class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        r=""
        while columnNumber>0:
            x=(columnNumber-1)%26
            r=r+chr(ord('A')+x)
            columnNumber=(columnNumber-1)//26
        return r[::-1]
