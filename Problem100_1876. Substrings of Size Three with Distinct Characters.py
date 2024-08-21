class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        c=0
        l=0
        r=2
        ss=set()
        while r<len(s):
            if len(set(s[l:r+1]))==3:
                c=c+1

            l=l+1
            r=r+1
        return c



