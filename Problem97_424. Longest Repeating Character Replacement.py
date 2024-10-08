class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d={}
        res=0
        l=0
        for r in range(len(s)):
            d[s[r]]=1+d.get(s[r],0)

            while ((r-l+1)-max(d.values()))>k:
                d[s[l]]-=1
                l=l+1
            res=max(res,r-l+1)
        return res
