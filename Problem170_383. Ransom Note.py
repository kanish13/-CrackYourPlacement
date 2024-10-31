class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in ransomNote:
            d[i]=d.get(i,0)+1
        for i in magazine:
            d[i]=d.get(i,0)-1
        for i in d.values():
            if i>0:
                return False
        return True
