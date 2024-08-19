class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=[0]*26
        n2=[0]*26
        for i in s1:
            n1[ord(i)-97]=n1[ord(i)-97]+1
        l=0
        r=len(s1)-1
        while r<len(s2):
            for i in s2[l:r+1]:
                n2[ord(i)-97]=n2[ord(i)-97]+1
            if n1==n2:
                return True
            else:
                n2=[0]*26
                l=l+1
                r=r+1
        return False


