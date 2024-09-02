class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        c=float("inf")
        s={}
        for i in text:
            if i in "balloon":
               s[i]=s.get(i,0)+1
        for i in 'ban':
            if s.get(i,0)<c:
                c=s.get(i,0)
        for i in 'lo':
            if s.get(i,0)<c*2:
                c=s.get(i,0)//2
        return c
        
