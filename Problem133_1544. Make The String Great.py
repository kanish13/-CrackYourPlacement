class Solution:
    def makeGood(self, s: str) -> str:
        x=[]
        for i in s:
            if x:
                if ord(i)-32==ord(x[-1]) or ord(i)==ord(x[-1])-32:
                    x.pop()
                else:
                    x.append(i)
            else:
                x.append(i)
        return "".join(x)    
