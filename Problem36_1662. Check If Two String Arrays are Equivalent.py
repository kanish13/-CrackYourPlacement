class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=0
        w2=0
        c1=0
        c2=0
        while w1<len(word1) and w2<len(word2):
            if word1[w1][c1]!=word2[w2][c2]:
                return False
            c1=c1+1
            c2=c2+1
            if c1>=len(word1[w1]):
                w1=w1+1
                c1=0
            if c2>=len(word2[w2]):
                w2=w2+1
                c2=0
        return w1==len(word1) and w2==len(word2)
            
