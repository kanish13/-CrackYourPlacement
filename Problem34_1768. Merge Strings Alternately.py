class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res=""
        l=0
        r=0
        while l<len(word1) and r<len(word2):
            res=res+word1[l]
            res=res+word2[r]
            l=l+1
            r=r+1
        while l<len(word1):
            res=res+word1[l]
            l=l+1
        while r<len(word2):
            res=res+word2[r]
            r=r+1
        return res

