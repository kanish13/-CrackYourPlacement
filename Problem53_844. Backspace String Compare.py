class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        c=0
        y=""
        for i in range(len(s)-1,-1,-1):
            if s[i]=="#":
                c=c+1
            else:
                if c==0:
                    y=y+s[i]
                else:
                    c=c-1
        c2=0
        z=""
        for i in range(len(t)-1,-1,-1):
            if t[i]=="#":
                c2=c2+1
            else:
                if c2==0:
                    z=z+t[i]
                else:
                    c2=c2-1
        return y==z
