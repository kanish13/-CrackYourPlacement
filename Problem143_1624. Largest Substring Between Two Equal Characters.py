class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        d={}
        maxi=-1
        for i in range(len(s)):
            if s[i] in d:
                if i-d[s[i]]-1>maxi:
                    maxi=i-d[s[i]]-1
            else:
                d[s[i]]=i
        return maxi

             
            

         
