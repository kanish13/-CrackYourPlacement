class Solution:
    def maxScore(self, s: str) -> int:
        zero=0
        one=list(s).count("1")
        l=0
        r=1
        res=0
        while r<len(s):
            if s[l]=="0":
                zero=zero+1
            else: 
                one=one-1
            if res<zero+one:
                res=zero+one
            l=l+1
            r=r+1
        return res
