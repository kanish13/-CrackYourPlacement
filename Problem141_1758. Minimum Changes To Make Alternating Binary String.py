class Solution:
    def minOperations(self, s: str) -> int:
        c=0
        for i in range(len(s)):
            if i%2==0:
                c=c+1 if s[i]=="1" else c
            else:
                c=c+1 if s[i]=="0" else c
        return min(c,len(s)-c)
