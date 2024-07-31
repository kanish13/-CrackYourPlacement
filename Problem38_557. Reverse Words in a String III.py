class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        for i in range(len(s)):
            r=len(s[i])-1
            y=""
            while r>-1:
                y=y+s[i][r]
                r=r-1
            s[i]=y
        return " ".join(s)
