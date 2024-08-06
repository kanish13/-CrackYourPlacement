class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        x=s1.split()
        y=s2.split()
        z=[]
        for i in x:
            if i not in y and x.count(i)==1:
                z.append(i)
        for i in y:
            if i not in x and y.count(i)==1:
                z.append(i)
        return z
