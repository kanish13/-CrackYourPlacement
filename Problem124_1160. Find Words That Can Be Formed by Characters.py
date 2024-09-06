class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c=Counter(chars)
        r=0
        for i in range(len(words)):
            f=0
            for j in range(len(words[i])):
                if c[words[i][j]]<words[i].count(words[i][j]):
                    f=1
                    break
            if f==0:
                r=r+len(words[i])
        return r


