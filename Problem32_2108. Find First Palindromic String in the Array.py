class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        a=""
        for i in range(len(words)):
            l=0
            r=len(words[i])-1
            c=0
            while l<=r:
                if words[i][l]==words[i][r] and l<r:
                    c=c+2
                elif words[i][l]==words[i][r] and l==r:
                    c=c+1
                l=l+1
                r=r-1

            if c==len(words[i]):
                a=words[i]
                return a
        return a
