class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if len(pattern)!=len(s.split()):
            return False
        x={}
        y={}
        for i,j in zip(pattern,s.split()):
            if i in x  and x[i]!=j :
                return False
            if j in y and y[j]!=i:
                return False
            x[i]=j
            y[j]=i
            
        return True
