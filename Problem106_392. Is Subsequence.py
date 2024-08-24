class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        l=0
        for i in t:
            if  l<len(s) and i==s[l]:
                l=l+1
        if l>=len(s):
            return True
        return False
        
