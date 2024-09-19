class Solution:
    def firstUniqChar(self, s: str) -> int:
        ss={}
        
        for i in s:
            ss[i]=ss.get(i,0)+1
        for i in range(len(s)):
            if ss[s[i]]==1:
                return i
        return -1
